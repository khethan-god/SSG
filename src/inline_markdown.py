import re
from textnode import TextNode, TextType

# We will use regular expressions to get the information 
# from markdown text to get both the `alt` text and `src` link;
# `\[(.*?)\]\((.*?)\)` this is a simple matching pattern, but might
# not work universally, so we need better regex.

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

# Now we need to write a function that will be able to convert 
# a raw markdown string into a list of TextNode objects.
# This function can handle bold, italic and code tags.

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        # we can have more than one inline element so we must have
        # odd number of values in the list `sections`
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i, val in enumerate(sections):
            if val == "":
                continue
            if i % 2 == 0: 
                # this gives val at indices [0, 2, 4, 6, 8, ...]
                # text_type as `TEXT`
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

# Now we need to use these functions to create text nodes
# from markdown text, these always operate on links and images
# so no need of a delimiter and text_type

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # 1. If the input is not of type TEXT
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        # 2. If the input has no links
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            # 3. If the split did not work properly
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            # 4. If the first part is not an empty string
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes



# Now using all the above functions we are going to write a simple function
# that is going to take markdown text as input and then convert that text
# into a list of TextNode instances

def text_to_textnodes(text):
    # first create a TextNode and since all these
    # functions accept a list as input lets pass them
    # as a list, because we need an iterable, not an object
    # as input to `split_nodes_delimiter`
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

