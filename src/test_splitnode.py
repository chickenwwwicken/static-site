import unittest
from splitnode import (
    split_nodes_delimiter, 
    extract_markdown_images,
    extract_markdown_links,
    )
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_front_split(self):
        print("running test_front_split...")
        node = TextNode("**This is text** with a bolded phrase in the front", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text", TextType.BOLD),
            TextNode(" with a bolded phrase in the front", TextType.NORMAL)
        ]
        # Comparing properties of the nodes.
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertEqual(result[i].text, expected[i].text)
            self.assertEqual(result[i].text_type, expected[i].text_type)



    
    def test_middle_split(self):
        print("running test_middle_split...")
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.NORMAL)
        ]
        # Comparing properties of the nodes.
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertEqual(result[i].text, expected[i].text)
            self.assertEqual(result[i].text_type, expected[i].text_type)




    def test_end_split(self):
        print("running test_end_split...")
        node = TextNode("This is text with a bolded phrase in **the end**", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a bolded phrase in ", TextType.NORMAL),
            TextNode("the end", TextType.BOLD)
        ]
        # Comparing properties of the nodes.
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertEqual(result[i].text, expected[i].text)
            self.assertEqual(result[i].text_type, expected[i].text_type)




    def test_no_closing_delimiter(self):
        print("running test_no_closing_delimiter...")
        node = TextNode("This is text _with no closing delimiter", TextType.NORMAL)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)




    def test_multiple_delimiters(self):
        print("running test_multiple_delimiters...")
        # start with a single node containing mixed delimiters
        initial_node = TextNode("This **is** a text with _two_ delimiters", TextType.NORMAL)

        # First, process bold delimiters
        intermediate_nodes = split_nodes_delimiter([initial_node], "**", TextType.BOLD)

        # Then process the italic delimiters on the result of the first split 
        final_nodes = split_nodes_delimiter(intermediate_nodes, "_", TextType.ITALIC)

        # Check result
        expected = [
            TextNode("This ", TextType.NORMAL),
            TextNode("is", TextType.BOLD),
            TextNode(" a text with ", TextType.NORMAL),
            TextNode("two", TextType.ITALIC),
            TextNode(" delimiters", TextType.NORMAL)
        ]
        # Comparing properties of the nodes.
        self.assertEqual(len(final_nodes), len(expected))
        for i in range(len(final_nodes)):
            self.assertEqual(final_nodes[i].text, expected[i].text)
            self.assertEqual(final_nodes[i].text_type, expected[i].text_type)

# ---------------------------------------------------------------------------
# 3.4 Tests for extracting links and images
    def test_extract_markdown_images(self):
        print("running text_extract_markdown_images...")
        matches = extract_markdown_images(
            "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_links(self):
        print("running text_extract_markdown_links...")
        matches = extract_markdown_links(
            "This is a text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

# ---------------------------------------------------------------------------
# 3.5 Tests for splitting links


if __name__ == '__main__':
    unittest.main()
