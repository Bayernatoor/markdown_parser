from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        else:
            delimiter_count = 0
            for char in old_node.text:
                if char == delimiter:
                    delimiter_count += 1
            if delimiter_count % 2 != 0:
                raise SyntaxError(f"Invalid markdown: missing {delimiter}")
            split = old_node.text.split(delimiter)
            for sub in split:
                index = split.index(sub)
                if sub == "":
                    continue
                if index % 2 != 0:
                    new_nodes.append(TextNode(sub, text_type))
                else:
                    new_nodes.append(TextNode(sub, text_type_text))
    return new_nodes
