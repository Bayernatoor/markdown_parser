import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_text_ne(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This  a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_text_type_ne(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This  a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url_exists(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev.com")
        self.assertTrue(node.url)

    def test_url_not_exists(self):
        node = TextNode("This is a text node", "bold")
        self.assertFalse(node.url)

    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

class TestHelpers(unittest.TestCase):
    def test_text_textnode_to_leafnode(self):
        textnode = TextNode("This is text", "text")
        text_to_leafnode = text_node_to_html_node(textnode)
        self.assertTrue((None, "This is Text", None), (f"{text_to_leafnode.tag},{text_to_leafnode.value},{text_to_leafnode.props}"))

    def test_bold_textnode_to_leafnode(self):
        textnode = TextNode("This is text", "bold")
        text_to_leafnode = text_node_to_html_node(textnode)
        self.assertTrue(("b", "This is Text", None), (f"{text_to_leafnode.tag},{text_to_leafnode.value},{text_to_leafnode.props}"))

    def test_italic_textnode_to_leafnode(self):
        textnode = TextNode("This is text", "italic")
        text_to_leafnode = text_node_to_html_node(textnode)
        self.assertTrue(("i", "This is Text", None), (f"{text_to_leafnode.tag},{text_to_leafnode.value},{text_to_leafnode.props}"))
    
    def test_code_textnode_to_leafnode(self):
        textnode = TextNode("This is text", "code")
        text_to_leafnode = text_node_to_html_node(textnode)
        self.assertTrue(("code", "This is Text", None), (f"{text_to_leafnode.tag},{text_to_leafnode.value},{text_to_leafnode.props}"))

    def test_link_textnode_to_leafnode(self):
        textnode = TextNode("This is text", "link", "https://www.google.com")
        text_to_leafnode = text_node_to_html_node(textnode)
        self.assertTrue(("a", "This is Text", {'href': 'https://www.google.com'}), (f"{text_to_leafnode.tag},{text_to_leafnode.value},{text_to_leafnode.props}"))

    def test_image_textnode_to_leafnode(self):
        textnode = TextNode("", "image", "http://www.link_to_img.com")
        text_to_leafnode = text_node_to_html_node(textnode)
        self.assertTrue(("img", "", {'src': 'http://www.link_to_img.com', 'alt': 'alt text'}), (f"{text_to_leafnode.tag},{text_to_leafnode.value},{text_to_leafnode.props}"))

if __name__ == "__main__":
    unittest.main()

