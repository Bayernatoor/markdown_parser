import re
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
    markdown_block = ["# Heading", "## Heading", "### Heading", "#### Heading",
                      "##### Heading", "###### Heading", "- Hi here", "* Why",
                      "```this is a code block```", ">single line quote",
                      ">double line quote\n>Here's the second line",
                      "This is a regular para with **bold** text",
                      "* unordered list\n- another but with a dash",
                      "1. Ordered list line 1\n2. line number 2\n3. line number3\n4. fourth line",
                      "1. ordered list line",
                      "Here's another one"
                      ]
    ordered = "1. Ordered list line 1\n4. fourth line"
    unordered = "* line number3\n- fourth line"
    paragrapg = "Just a regular para with `code` and *italic*"
    code = "``` WHY CODE ? ```"
    quote = "> Hello there"
    heading = "## Heading Hello"

    return block_to_block_type(ordered)



print(main())
