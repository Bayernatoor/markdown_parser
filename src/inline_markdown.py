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
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        extracted_images = extract_markdown_images(original_text)
        if len(extracted_images) == 0:
            new_nodes.append(node)
            continue
        for extracted in extracted_images:
            split = original_text.split(f"![{extracted[0]}]({extracted[1]})", 1)
            if len(split) != 2:
                raise SyntaxError("Invalid Markdown, image not closed")
            if not split[0].isspace():
                new_nodes.append(TextNode(split[0], text_type_text))

            new_nodes.append(TextNode(extracted[0], text_type_image,
                                      extracted[1]))
            original_text = split[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        extracted_links = extract_markdown_links(original_text)
        if len(extracted_links) == 0:
            new_nodes.append(node)
            continue
        for extracted in extracted_links:
            split = original_text.split(f"[{extracted[0]}]({extracted[1]})", 1)
            if len(split) != 2:
                raise SyntaxError("Invalid Markdown, link not closed")
            if not split[0].isspace():
                new_nodes.append(TextNode(split[0], text_type_text))

            new_nodes.append(TextNode(extracted[0], text_type_link,
                                      extracted[1]))

            original_text = split[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def text_to_textnodes(text):
    text_node = TextNode(text, text_type_text)
    new_node = []

    bold = split_nodes_delimiter([text_node], "**", text_type_bold)
    italic = split_nodes_delimiter(bold, "*", text_type_italic)
    code = split_nodes_delimiter(italic, '`', text_type_code)
    images = split_nodes_image(code)
    links = split_nodes_link(images)
    new_node.extend(links)

    return new_node
