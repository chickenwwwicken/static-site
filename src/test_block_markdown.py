import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_trailing_blanklines(self):
        md = """
First Block

Second Block

"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "First Block",
                "Second Block"
            ],
            blocks,
        )

    def test_multiblock(self):
        md = """
this is the first paragraph

this is the second paragraph
that continues on a new line

- first item
- second item
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "this is the first paragraph",
                "this is the second paragraph\nthat continues on a new line",
                "- first item\n- second item"
            ],
            blocks,
        )

    def test_multiple_blanklines(self):
        md = """
A


B
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "A",
                "B"
            ],
            blocks,
        )

    def test_only_blanklines(self):
        md = """


  

"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual([], blocks,)

if __name__ == "__main__":
    unittest.main()
