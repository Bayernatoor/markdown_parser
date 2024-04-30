from inline_markdown import text_to_textnodes, split_nodes_image, split_nodes_link
from textnode import TextNode
from blocks import markdown_to_blocks

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def main():
    block = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

    return markdown_to_blocks(block)


print(main())
