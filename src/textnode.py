from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    NORMAL = 'normal' 
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return ( 
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

# Convert TextNode to HTMLNode
def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case(TextType.NORMAL):
            return LeafNode(value=text_node.text)

        case(TextType.BOLD):
            return LeafNode("b", text_node.text)
        
        case(TextType.ITALIC):
            return LeafNode("i", text_node.text)
        
        case(TextType.CODE):
            return LeafNode("code", text_node.text)
        
        case(TextType.LINK):
            link_props = {"href": text_node.url}
            return LeafNode("a", text_node.text, link_props)
        
        case(TextType.IMAGE):
            image_props = {"src": text_node.url, "alt": text_node.text}
            return LeafNode("img", "", image_props)
        
        case _:
            raise Exception('Invalid Type') 
