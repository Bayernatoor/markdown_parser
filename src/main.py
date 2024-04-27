from textnode import TextNode, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode, ParentNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def main():
    #textnode_one = TextNode("A text node", "italic", "https://www.boot.dev")
    #htmlnode_one = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    #print(textnode_one)
    #node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    node = [
           TextNode("This is a **bold block** word", text_type_text), 
           TextNode("`This` is a text with a `code block` word", text_type_text),
           LeafNode("a", "link", None)
           ]

    text_new = split_nodes_delimiter(node, "`", text_type_code)

    return text_new


print(main())



