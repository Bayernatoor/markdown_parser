import re
import unittest
from inline_markdown import text_to_textnodes, split_nodes_image, split_nodes_link
from textnode import TextNode
from markdown_blocks import (markdown_to_blocks,
                             block_to_block_type,
                             block_type_paragraph,
                             block_type_ordered_list,
                             block_type_unordered_list,
                             block_type_quote,
                             block_type_heading,
                             block_type_code
                             )

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def main():
    markdown_blocks = [
            "# Heading", "## Heading", "### Heading", "#### Heading",
            "##### Heading", "###### Heading", "- Hi here", "* Why",
            "```this is a code block```", ">single line quote",
            ">double line quote\n>Here's the second line",
            "This is a regular para with **bold** text",
            "* unordered list\n- another but with a dash",
            "1. Ordered list line 1\n2. line number 2\n3. line number3\n4. fourth line",
            "1. ordered list line",
            "Here's another one"
            ]
    actual = [
           'heading',
           'heading',
           'heading',
           'heading',
           'heading',
           'heading',
           'unordered_list',
           'unordered_list',
           'code',
           'quote',
           'quote',
           'paragraph',
           'unordered_list',
           'ordered_list',
           'ordered_list',
           'paragraph'
           ]

    block_types = []
    for block in markdown_blocks:
        result = block_to_block_type(block)
        block_types.append(result)

    return block_types == actual



print(main())
