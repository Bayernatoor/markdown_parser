import unittest
from markdown_blocks import markdown_to_blocks


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


if __name__ == "__main__":
    unittest.main()
