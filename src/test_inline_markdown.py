import unittest

from htmlnode import LeafNode
from inline_markdown import split_nodes_delimiter

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_code_textnode(self):
        node = TextNode("This is a text with a `code block` word", text_type_text)
        result = [TextNode("This is a text with a ", "text", None), TextNode("code block", "code", None), TextNode(" word", "text", None)]
        self.assertEqual(result, split_nodes_delimiter([node], "`", text_type_code))

    def test_italic_textnode(self):
        node = TextNode("This is a text with two *italic* words, *crazy eh!*", text_type_text)
        result = [TextNode("This is a text with two ", "text", None), TextNode("italic", "italic", None), TextNode(" words, ", "text", None), TextNode("crazy eh!", "italic", None)]
        self.assertEqual(result, split_nodes_delimiter([node], "*", text_type_italic))

    def test_bold_textnode(self):
        node = TextNode("This is a text with a **bolded** word", text_type_text)
        result = [TextNode("This is a text with a ", "text", None), TextNode("bolded", "bold", None), TextNode(" word", "text", None)]
        self.assertEqual(result, split_nodes_delimiter([node], "**", text_type_bold))

    def test_incorrect_delimiter(self):
        node = TextNode("This is a text with a **bolded** word", text_type_text)
        result = [TextNode("This is a text with a **bolded** word", "text", None)]
        self.assertEqual(result, split_nodes_delimiter([node], "`", text_type_bold))

    def test_missing_closing_delimiter(self):
        node = [
           TextNode("This is a text with a `code block word", text_type_text),
           ]

        self.assertRaises(SyntaxError, split_nodes_delimiter, node, "`", text_type_bold)

    def test_multiple_nodes(self):
        node = [
           TextNode("This is a **bold block** word", text_type_text), 
           TextNode("`This` is a text with a `code block` word", text_type_text),
           TextNode("Let's write some `code`", text_type_text),
           ]
        result = [TextNode("This is a **bold block** word", "text", None), TextNode("This", "code", None), TextNode(" is a text with a ", "text", None), TextNode("code block", "code", None), TextNode(" word", "text", None), TextNode("Let's write some ", "text", None), TextNode("code", "code", None)]
        self.assertEqual(result, split_nodes_delimiter(node, "`", text_type_code))

if __name__ == "__main__":
    unittest.main()
