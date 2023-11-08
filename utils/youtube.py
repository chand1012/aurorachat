import re


def get_youtube_video_id(url: str) -> str:
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/|v\/)|youtu\.be\/|youtube\.com\/(?:user\/.*\/|playlist\?list=))?(?P<id>[A-Za-z0-9_-]{11})'
    match = re.search(pattern, url)

    if match:
        return match.group('id')
    else:
        return None


if __name__ == '__main__':
    # Test cases
    url1 = 'This is a test case for a youtube video message! https://www.youtube.com/watch?v=abcdefghijk'
    url2 = 'https://youtu.be/abcdefghijk'
    url3 = 'https://www.youtube.com/embed/abcdefghijk'
    url4 = "There is no content here."
    url5 = "There are multiple youtube videos here. https://www.youtube.com/watch?v=abcdefghijk https://www.youtube.com/watch?v=zxcvbnmasdf"

    assert get_youtube_video_id(url1) == "abcdefghijk"  # Output: abcdefghijk
    assert get_youtube_video_id(url2) == "abcdefghijk"  # Output: abcdefghijk
    assert get_youtube_video_id(url3) == "abcdefghijk"  # Output: abcdefghijk
    assert get_youtube_video_id(url4) == None  # Output: None
    assert get_youtube_video_id(url5) == "abcdefghijk"  # Output: None
