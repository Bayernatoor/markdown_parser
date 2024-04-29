import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
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


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        num_of_images = 0
        extracted_images = extract_markdown_images(node.text)
        num_of_images = len(extracted_images)
        if num_of_images == 0:
            new_nodes.append(node)
        for extracted in extracted_images:
            split = node.text.split(f"![{extracted[0]}]({extracted[1]})", 1)
            node.text = split[1]
            if not split[0].isspace():
                new_nodes.append(TextNode(split[0], text_type_text))

            new_nodes.append(TextNode(extracted[0], text_type_image,
                                      extracted[1]))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        num_of_links = 0
        extracted_links = extract_markdown_links(node.text)
        num_of_links = len(extracted_links)
        if num_of_links == 0:
            new_nodes.append(node)
        for extracted in extracted_links:
            split = node.text.split(f"[{extracted[0]}]({extracted[1]})", 1)
            node.text = split[1]
            if not split[0].isspace():
                new_nodes.append(TextNode(split[0], text_type_text))

            new_nodes.append(TextNode(extracted[0], text_type_link,
                                      extracted[1]))

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
