import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("cat", "Bak", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href=\"https://www.google.com\" target=\"_blank\"')


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        p_node = LeafNode("p", "This is a paragraph of text.")
        a_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(p_node.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(a_node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_tag_none(self):
        p_node = LeafNode(None, "This is a paragraph of text.")
        self.assertTrue(p_node.to_html(), "This is a paragraph of text.")

    def test_repr(self):
        a_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
                "LeafNode(a, Click me!, {'href': 'https://www.google.com'})", repr(a_node)
                )

class TestParentNode(unittest.TestCase):
    def test_repr(self):
        a_node = ParentNode(
                    "p",
                        [
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text"),
                        ],
                    )
        self.assertEqual(
                "ParentNode(p, [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], None)", repr(a_node)
                )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )



if __name__ == "__main__":
    unittest.main()
