class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_props = ""
        if len(self.props) >= 0:
            for key, value in self.props.items():
                html_props += f" {key}=\"{value}\""

        return html_props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, \
                          {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value must not be None")
        elif self.tag is None:
            return self.value
        else:
            opening_tag = f"<{self.tag}>"
            closing_tag = f"</{self.tag}>"
            if self.props:
                opening_tag_w_props = f"<{self.tag}{super().props_to_html()}>"
                return f"{opening_tag_w_props}{self.value}{closing_tag}"
            else:
                return f"{opening_tag}{self.value}{closing_tag}"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML, missing tag")
        if self.children is None:
            raise ValueError("Invalid ParentNode, missing children")
        result = ""
        for i in self.children:
            result += i.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
