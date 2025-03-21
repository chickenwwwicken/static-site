import unittest
from extract_links import extract_markdown_images
from extract_links import extract_markdown_links

class TestExtractLinks(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
