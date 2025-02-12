from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    ITALIC = "italic"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

# This function accepts an instance of the `TextNode` class and 
# helps in converting them to HTML tags
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)  # normal text, convert to raw html
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        # here we pass the property which is a link
        return LeafNode("a", text_node.text, {"href":text_node.url})
    if text_node.text_type == TextType.IMAGE:
        # here we use the img tag with empty value, since link and text are properties
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(None, text_node.text)
    raise ValueError(f"invalid text type: {text_node.text_type}")
