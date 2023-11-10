from io import BytesIO


class FileBuffer(BytesIO):
    def __init__(self, content: bytes, name: str = None):
        super().__init__(content)
        self.seek(0)
        self.name = name or "file"
