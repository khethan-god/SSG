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