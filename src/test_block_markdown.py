import unittest
from block_markdown import BlockType, block_to_block_type, markdown_to_blocks

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


# ---------------------------------------------------------
# ----------------------blocktypes-------------------------
# ---------------------------------------------------------

    def test_paragraph_type(self):
        md = """
example paragraph
example paragraph
"""
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.PARAGRAPH, block_type)


    def test_quote_type(self):
        md = """
>example quote
> example quote
> example quote
"""
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.QUOTE, block_type)


    def test_ordered_type(self):
        md = """
1. ordered
2. list
3. that
4. should
5. pass
6. the test
"""
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)


    def test_unordered_type(self):
        md = """
- unordered
- list
- of items
"""
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)


    def test_heading1_type(self):
        md = """
# Heading 1
"""
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)


    def test_heading2_type(self):
        md = """
#### Heading 4
"""
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)


    def test_code_type(self):
        md = """
```
example code
```
"""
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.CODE, block_type)


if __name__ == "__main__":
    unittest.main()
