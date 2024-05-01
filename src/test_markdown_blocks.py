import unittest

from markdown_blocks import (markdown_to_blocks,
                             block_to_block_type,
                             block_type_code,
                             block_type_heading,
                             block_type_quote,
                             block_type_unordered_list,
                             block_type_ordered_list,
                             block_type_paragraph
                             )


class TextBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        block = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        result = ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items']

        self.assertEqual(result, markdown_to_blocks(block))

    def test_big_markdown_to_blocks_with_newlines(self):
        block = """
This is **bolded** paragraph
This is **bolded** paragraph

This is **bolded** paragraph

""

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
This is **bolded** paragraph
* with items


* with items

* with items
"""
        result = ['This is **bolded** paragraph\nThis is **bolded** paragraph', 'This is **bolded** paragraph', '""', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\nThis is **bolded** paragraph\n* with items', '* with items', '* with items']

        self.assertEqual(result, markdown_to_blocks(block))

    def test_block_to_block_type_ordered(self):
        ordered = "1. Ordered list line 1\n2. fourth line"

        self.assertEqual(block_type_ordered_list, block_to_block_type(ordered))

    def test_block_to_block_type_unordered(self):
        unordered = "* line number3\n- fourth line"

        self.assertEqual(block_type_unordered_list,
                         block_to_block_type(unordered))

    def test_block_to_block_type_paragraph(self):
        paragraph = "Just a regular para with `code` and *italic*"

        self.assertEqual(block_type_paragraph, block_to_block_type(paragraph))

    def test_block_to_block_type_code(self):
        code = "``` WHY CODE ? ```"

        self.assertEqual(block_type_code, block_to_block_type(code))

    def test_block_to_block_type_quote(self):
        quote = "> Hello there"

        self.assertEqual(block_type_quote, block_to_block_type(quote))

    def test_block_to_block_type_heading(self):
        heading = "## Heading Hello"

        self.assertEqual(block_type_heading, block_to_block_type(heading))

    def text_block_type_all_cases(self):
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

        self.assertListEqual(result, actual)

    def test_block_to_block_type_incorrect_ordered(self):
        incorrect_ordered = "1. Ordered list line 1\n3. fourth line\n2. another line"

        self.assertEqual(block_type_paragraph, block_to_block_type(incorrect_ordered))


if __name__ == "__main__":
    unittest.main()
