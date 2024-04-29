from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_link, split_nodes_image 

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def main():
    #image_text = "Here we have an image of a duck ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png) and a third ![third_image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
    #node = [
    #        TextNode(
    #            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    #            text_type_text,),
    #        TextNode(
    #            "Here we have an image of a duck ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)",
    #            text_type_text,)
    #        ]
    #nodes = [
    #        TextNode(
    #            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    #            text_type_text,)]

    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    text_node = TextNode(text, text_type_text) 
    
    
    bold = split_nodes_delimiter([text_node], "**", text_type_bold)
    new_node = []

    print(f"bold: {bold}")
    italic =  split_nodes_delimiter(bold, "*", text_type_italic)
    print(f"italic: {italic}")
    code = split_nodes_delimiter(italic, '`', text_type_code)
    print(f"code: {code}")
    images = split_nodes_image(code)
    print(f"images: {images}")
    links = split_nodes_link(images)
    print(f"links: {links}")

    new_node.extend(links)

    #return new_node

print(main())
