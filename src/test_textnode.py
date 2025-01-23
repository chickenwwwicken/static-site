import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.text1_italic_urln = TextNode('text1', TextType.ITALIC)
        self.text1_italic_url1 = TextNode('text1', TextType.ITALIC, 'www.url1.com')
        self.text1_italic_url2 = TextNode('text1', TextType.ITALIC, 'www.url2.com')
        self.text1_bold_urln = TextNode('text1', TextType.BOLD)
        self.text1_bold_url1 = TextNode('text1', TextType.BOLD, 'www.url1.com')
        self.text1_bold_url2 = TextNode('text1', TextType.BOLD, 'www.url2.com')
        self.text2_italic_urln = TextNode('text2', TextType.ITALIC)
        self.text2_italic_url1 = TextNode('text2', TextType.ITALIC, 'www.url1.com')
        self.text2_italic_url2 = TextNode('text2', TextType.ITALIC, 'www.url2.com')
        self.text2_bold_urln = TextNode('text2', TextType.BOLD)
        self.text2_bold_url1 = TextNode('text2', TextType.BOLD, 'www.url1.com')
        self.text2_bold_url2 = TextNode('text2', TextType.BOLD, 'www.url2.com')              

    def test_eq(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        self.assertNotEqual(self.text1_italic_urln, self.text1_italic_url1)

    def test_url_eq(self):
        self.assertEqual(self.text1_italic_url1.url, self.text1_bold_url1.url)

    def test_url_not_eq(self):
        self.assertNotEqual(self.text1_italic_url1.url, self.text1_italic_url2.url)

    def test_text_eq(self):
        self.assertEqual(self.text1_italic_urln.text, self.text1_bold_urln.text)
    
    def test_text_not_eq(self):
        self.assertNotEqual(self.text1_italic_urln.text, self.text2_italic_urln.text)

    def test_texttype_equal(self):
        self.assertEqual(self.text1_italic_url1.text_type, self.text1_italic_url2.text_type)

    def test_texttype_not_equal(self):
        self.assertNotEqual(self.text1_italic_url1.text_type, self.text1_bold_url1.text_type)

if __name__ == '__main__':
    unittest.main()
