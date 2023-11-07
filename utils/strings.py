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
