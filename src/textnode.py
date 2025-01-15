from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "url"
    IMAGE = "img"

class TextNode:
    def __init__(self, text, text__type, url=None):
        self.text = text
        self.text__type = text__type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text__type == other.text__type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text__type}, {self.url})"