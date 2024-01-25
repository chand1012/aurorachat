import re


def split_messages(content, max_len=2000):
    split = content.split("\n")
    responses = []
    current = ""
    for line in split:
        if len(current) + len(line) > max_len:
            responses.append(current)
            current = ""
        current += line + "\n"
        responses.append(current)
    return responses


def truncate_string(string):
    if len(string) <= 50:
        return string
    else:
        return string[:50] + '...'


def split_string_on_space(s: str, n: int) -> list[str]:
    words = s.split(' ')
    result = []
    current_line = ''

    for word in words:
        if len(current_line) + len(word) + 1 > n:
            result.append(current_line.strip())
            current_line = ''

        current_line += ' ' + word

    if current_line.strip():
        result.append(current_line.strip())

    return result


def split_text_into_chunks(text, max_length=1024) -> list[str]:
    """
    Splits the text into chunks of up to max_length characters.
    Each chunk ends with a period and is as close to max_length characters as possible.
    """
    pattern = r'.{1,' + str(max_length) + r'}(?<=\.)\s'
    chunks = re.findall(pattern, text, flags=re.DOTALL)

    # Handling the case where the last chunk might not end with a period
    if text.endswith('.') and text not in chunks[-1]:
        # Append the last incomplete chunk to the second last chunk
        chunks[-2] += chunks[-1]
        del chunks[-1]

    return [chunk.strip() for chunk in chunks]
