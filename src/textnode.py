from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "normal"
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
        return (
            self.text == other.text
            and self.text__type == other.text__type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text__type}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text__type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text).to_html()
        case TextType.BOLD:
            return LeafNode("b", text_node.text).to_html()
        case TextType.ITALIC:
            return LeafNode("i", text_node.text).to_html()
        case TextType.CODE:
            return LeafNode("code", text_node.text).to_html()
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url}).to_html()
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text}).to_html()
        case _:
            raise Exception('Invalid Node type')
