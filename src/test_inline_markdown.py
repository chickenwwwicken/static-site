import unittest
from inline_markdown import text_to_textnodes, split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


# ---------------------------------------------------------
# -------------------bold-italic-code----------------------
# ---------------------------------------------------------

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )


    # ---------------------------------------------------------
    # -------------------links-images--------------------------
    # ---------------------------------------------------------


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "This is text with a [link1](https://www.link1.com) and another [link2](https://www.link2.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "https://www.link1.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "link2", TextType.LINK, "https://www.link2.com"
                ),
            ],
            new_nodes,
        )


    # ---------------------------------------------------------
    # -------------------final-final---------------------------
    # ---------------------------------------------------------

    def test_text_to_textnodes_plain(self):
        text = "hello there"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 1
        assert nodes[0].text == "hello there"
        assert nodes[0].text_type == TextType.TEXT

    def test_text_to_textnodes_bold(self):
        text = "this is **bold** text"
        nodes = text_to_textnodes(text)

        assert len(nodes) == 3
        assert nodes[0].text == "this is "
        assert nodes[0].text_type == TextType.TEXT

        assert nodes[1].text == "bold"
        assert nodes[1].text_type == TextType.BOLD

    def test_text_to_textnodes_italic_and_code(self):
        text = "_hi_ `code`"
        nodes = text_to_textnodes(text)

        assert any(n.text_type == TextType.ITALIC for n in nodes)
        assert any(n.text_type == TextType.CODE for n in nodes)

    def test_text_to_textnodes_image(self):
        text = "look ![alt text](https://example.com/img.png)"
        nodes = text_to_textnodes(text)

        img_node = [n for n in nodes if n.text_type == TextType.IMAGE][0]
        assert img_node.text == "alt text"
        assert img_node.url == "https://example.com/img.png"

    def test_text_to_textnodes_link(self):
        text = "see [Boot](https://boot.dev)"
        nodes = text_to_textnodes(text)

        link_node = [n for n in nodes if n.text_type == TextType.LINK][0]
        assert link_node.text == "Boot"
        assert link_node.url == "https://boot.dev"

    def test_text_to_textnodes_all_features(self):
        text = "This is **bold** and _italic_ with `code` and ![alt](https://example.com/i.png) and a [link](https://example.com)"

        nodes = text_to_textnodes(text)

        assert len(nodes) == 10

        assert nodes[0].text == "This is "
        assert nodes[0].text_type == TextType.TEXT

        assert nodes[1].text == "bold"
        assert nodes[1].text_type == TextType.BOLD

        assert nodes[2].text == " and "
        assert nodes[2].text_type == TextType.TEXT

        assert nodes[3].text == "italic"
        assert nodes[3].text_type == TextType.ITALIC

        assert nodes[4].text == " with "
        assert nodes[4].text_type == TextType.TEXT

        assert nodes[5].text == "code"
        assert nodes[5].text_type == TextType.CODE

        assert nodes[6].text == " and "
        assert nodes[6].text_type == TextType.TEXT

        assert nodes[7].text == "alt"
        assert nodes[7].url == "https://example.com/i.png"
        assert nodes[7].text_type == TextType.IMAGE

        assert nodes[8].text == " and a "
        assert nodes[8].text_type == TextType.TEXT

        assert nodes[9].text == "link"
        assert nodes[9].url == "https://example.com"
        assert nodes[9].text_type == TextType.LINK



if __name__ == "__main__":
    unittest.main()
