import unittest
from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


# Test class by chicken
class TestTextNode(unittest.TestCase):
    def setUp(self):

        self.italic_node = TextNode('italic text', TextType.ITALIC)
        self.bold_node = TextNode('some bold text', TextType.BOLD)
        self.normal_node = TextNode('some text', TextType.NORMAL)
        self.code_node = TextNode('somecode123', TextType.CODE)
        self.link_node1 = TextNode('link1', TextType.LINK, 'www.url1.com')
        self.image_node1 = TextNode('image1', TextType.IMAGE, 'www.url1.com')

    def test_eq(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node, node2)

    # normal node
    def test_text_node_to_html_node_normal(self):
        text_node = TextNode("This is a text", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.value, "This is a text")
        self.assertIsNone(html_node.tag)

    # bold node
    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    # italic node
    def test_text_node_to_html_node_italic(self):
        html_node = text_node_to_html_node(self.italic_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic text")
    
    # code node
    def test_text_node_to_html_node_code(self):
        html_node = text_node_to_html_node(self.code_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "somecode123")

    # Link node 
    def test_text_node_to_html_node_link(self):
        html_node = text_node_to_html_node(self.link_node1)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "www.url1.com"})
    
    # image node
    def test_text_node_to_html_node_image(self):
        html_node = text_node_to_html_node(self.image_node1)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "www.url1.com", "alt": "image1"})


# Test Class by bootdev
class TestTextNodeBoot(unittest.TestCase):
    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == '__main__':
    unittest.main()
