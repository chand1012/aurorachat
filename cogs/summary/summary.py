from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi

from ai import count_tokens
from cogs.summary.constants import SYSTEM_PROMPT
from utils import get_youtube_video_id, split_string_on_space


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
        summary = generate_summary(0, text)
    summary = summary.strip()
    while len(summary) + 33 > 2000:
        summary = generate_summary(o, summary)
    return transcript, summary
