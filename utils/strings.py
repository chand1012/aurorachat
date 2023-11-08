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
