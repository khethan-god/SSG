from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        return (
            self.text == other.text and \
            self.text_type.value == other.text_type.value and \
            self.url == other.url
        )
    def __str__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'
    def __repr__(self):
        return str(self)
    

def text_node_to_html_node(text_node):
    # This function should convert a text node to a leaf node
    match text_node.text_type:
        case TextType.TEXT: return LeafNode(None, text_node.text)
        case TextType.BOLD: return LeafNode("b", text_node.text)
        case TextType.ITALIC: return LeafNode("i", text_node.text)
        case TextType.CODE: return LeafNode("code", text_node.text)
        case TextType.LINK: return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE: return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case default: raise  ValueError(f"invalid text type: {text_node.text_type}")
        