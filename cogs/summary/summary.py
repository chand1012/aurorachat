from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
from sqlmodel import Session, select

from db.models import Summary, Request
from ai import count_tokens
from cogs.summary.constants import SYSTEM_PROMPT
from utils import split_string_on_space


def generate_summary(o: OpenAI, prompt: str):
    resp = o.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[{
            'role': "system",
            'content': SYSTEM_PROMPT
        }, {
            'role': "user",
            'content': prompt
        }]
    )
    return resp.choices[0].message.content


def summarize(o: OpenAI, video_id: str):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = ''
    for line in transcript:
        text += line['text'] + ' '

    max_tokens = 15000
    tokens = count_tokens(text)
    summary = ''
    if tokens > max_tokens:
        prompts = split_string_on_space(text, max_tokens)
        for prompt in prompts:
            summary += generate_summary(o, prompt) + ' '
    else:
        summary = generate_summary(o, text)
    summary = summary.strip()
    while len(summary) + 33 > 2000:
        summary = generate_summary(o, summary)
    return transcript, summary


def process_summary(session: Session, o: OpenAI, video_id: str, request: Request):
    stmt = select(Summary).where(Summary.yt_id == video_id)
    s = session.exec(stmt).first()
    if s:
        return s.transcript, s.summary, True
    transcript, summary = summarize(o, video_id)
    # save the summary
    s = Summary(yt_id=video_id, summary=summary,
                transcript=transcript, url=f'https://youtu.be/{video_id}', req_id=request.id)
    session.add(s)
    session.commit()
    return transcript, summary, False
