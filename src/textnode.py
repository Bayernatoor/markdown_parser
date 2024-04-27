from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    types = ["text", "bold", "italic", "code", "link", "image"]

    if text_node.text_type not in types:
        raise ValueError("Not a valid HTML type")
    elif text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode("img", "",  {"src": text_node.url, "alt": text_node.text})


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for oldnode in old_nodes:
        if not isinstance(oldnode, TextNode):
            new_nodes.append(oldnode)
        else:
            delimiter_count = 0
            for char in oldnode.text:
                if char == delimiter:
                    delimiter_count += 1
            if delimiter_count % 2 != 0:
                raise SyntaxError(f"Invalid markdown: missing {delimiter}")
            split = oldnode.text.split(delimiter)
            for sub in split:
                index = split.index(sub)
                if sub == "":
                    continue
                if index % 2 != 0:
                    new_nodes.append(TextNode(sub, text_type))
                else:
                    new_nodes.append(TextNode(sub, text_type_text))
    return new_nodes