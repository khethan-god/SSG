class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              # all tags
        self.value = value          # the values within tags
        self.children = children    # instances of HTMLNodes 
        self.props = props          # attributes of the tags
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props:
            attributes = ''
            for keys in self.props:
                attributes += f' {keys}="{self.props[keys]}"'
            return attributes
        return ""
    
    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, property={self.props})'
    

# First child class which represents the leaf nodes
# It will not have any children
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("invalid HTML: no value")
        if not self.tag:
            return self.value
        if not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, property={self.props})"


# Second child class which represents the parent nodes
# It must have children
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, property={self.props})"
    
    def to_html(self):
        if not self.tag: raise ValueError("invalid HTML: no tag found")
        if not self.children: raise ValueError("invalid HTML: no inline tags found")
        children_html = ""
        # Here if the child nodes have parent nodes within them then
        # recursion happens, if not then the `.to_html()` function of the
        # leaf node is called
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"