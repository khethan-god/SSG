from textnode import TextNode, TextType

def main():
    link = TextType.LINK
    text_node = TextNode('This is some anchor text', link, 'https://www.boot.dev')
    print(text_node)

main()