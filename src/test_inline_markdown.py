import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)


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

    def test_extract_markdown_images(self):
        image_text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"

        self.assertListEqual([
                            ('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), 
                            ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')
                            ], extract_markdown_images(image_text)

                             )

    def test_extract_markdown_links(self):
        link_text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"

        self.assertEqual([
                        ('link', 'https://www.example.com'),
                        ('another', 'https://www.example.com/another')],
                         extract_markdown_links(link_text))

    def test_split_node_image(self):
        node = [
                TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        text_type_text,)]

        self.assertListEqual(
            [
                TextNode("This is text with an ", "text", None),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and ", "text", None),
                TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
            ],
            split_nodes_image(node))

    def test_multi_split_node_image(self):
        node = [
                TextNode(
                    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                    text_type_text,),
                TextNode(
                    "Here we have an image of a duck ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)",
                    text_type_text,)
                ]

        self.assertListEqual(
            [
                TextNode("This is text with an ", "text", None),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and ", "text", None),
                TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
                TextNode("Here we have an image of a duck ", "text", None),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and ", "text", None),
                TextNode("another", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png"),
            ],
            split_nodes_image(node))

    def test_split_node_image_whitespace(self):
        node = [
                TextNode(
                "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)  ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                text_type_text,)]

        self.assertListEqual(
            [
                TextNode("This is text with an ", "text", None),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
            ],
            split_nodes_image(node))

    def test_split_node_image_no_image(self):
        node = [
                TextNode(
                "This is text with an (https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
                text_type_text,)]

        self.assertListEqual(
            [
                TextNode("This is text with an (https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)", "text", None),
            ],
            split_nodes_link(node))

    def test_split_node_link(self):
        node = [
                TextNode(
                    "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                    text_type_text,)]

        self.assertListEqual(
            [
                TextNode("This is text with an ", "text", None),
                TextNode("link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and ", "text", None),
                TextNode("second link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
            ],
            split_nodes_link(node))

    def test_multi_split_node_link(self):
        node = [
                TextNode(
                    "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                    text_type_text,),
                TextNode(
                    "Here we have a link of a duck [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)",
                    text_type_text,)
                ]

        self.assertListEqual(
            [
                TextNode("This is text with an ", "text", None),
                TextNode("link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and ", "text", None),
                TextNode("second link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
                TextNode("Here we have a link of a duck ", "text", None),
                TextNode("link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and ", "text", None),
                TextNode("another", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png"),
            ],
            split_nodes_link(node))

    def test_split_node_link_whitespace(self):
        node = [
                TextNode(
                "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)  [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                text_type_text,)]

        self.assertListEqual(
            [
                TextNode("This is text with an ", "text", None),
                TextNode("link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode("second link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
            ],
            split_nodes_link(node))

    def test_split_node_link_no_link(self):
        node = [
                TextNode(
                    "This is text with an (https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
                    text_type_text,)]

        self.assertListEqual(
            [
                TextNode("This is text with an (https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)", "text", None),
            ],
            split_nodes_link(node))

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        result = [
                TextNode("This is ", "text", None),
                TextNode("text", "bold", None),
                TextNode(" with an ", "text", None),
                TextNode("italic", "italic", None),
                TextNode(" word and a ", "text", None),
                TextNode("code block", "code", None),
                TextNode(" and an ", "text", None),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://boot.dev"),
            ]

        self.assertListEqual(result, text_to_textnodes(text))

if __name__ == "__main__":
    unittest.main()


    #nodes = [
    #        TextNode(
    #"This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)   ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    #text_type_text,)]
    #        TextNode(
    #"Here we have an image of a duck ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)   ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png) and a third ![third_image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
    #text_type_text,)]
