from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    html_node = HTMLNode("p", "This is my first html project", None, None)
    
    print(node)
    print(html_node)


main()
