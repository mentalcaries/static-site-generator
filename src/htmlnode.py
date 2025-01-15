class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this")

    def props_to_html(self):
        all_attributes = ""
        if self.props:
            for key in self.props:
                all_attributes += f" {key}='{self.props[key]}'"
        return all_attributes
    
    def __repr__(self):
        return f"HTML Node: tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.value = value

    def to_html(self):
        if not self.value:
            raise ValueError("Value is required")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"