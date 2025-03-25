class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    def props_to_html(self):
        # This function should return a string of HTML attributes
        # based on the props dictionary
        if self.props is None: return ''
        attribute = ''
        for key, value in self.props.items():
            attribute += f' {key}="{value}"'
        return attribute
    def __str__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
    def __repr__(self):
        return str(self)
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value is None: raise ValueError("invalid HTML: no value")
        if self.tag is None: return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __str__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    def __repr__(self):
        return str(self)


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None: raise ValueError("Invalid HTML: no tag")
        if self.children is None: raise ValueError("Invalid HTML: no children")
        child_nodes_to_string = ''
        for child in self.children:
            child_nodes_to_string += child.to_html() # since child is an instance of LeafNode
        return f"<{self.tag}>{child_nodes_to_string}</{self.tag}>"
    def __str__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    def __repr__(self):
        return str(self)