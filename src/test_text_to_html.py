import unittest
from text_to_html import markdown_to_html_node

class TestTextToHTML(unittest.TestCase):



    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )




    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_multiple_headings(self):
        md = """
# H1 Heading

## H2 Heading

### H3 with **bold**

#### H4 Heading

##### H5 Heading

###### H6 Heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>H1 Heading</h1><h2>H2 Heading</h2><h3>H3 with <b>bold</b></h3><h4>H4 Heading</h4><h5>H5 Heading</h5><h6>H6 Heading</h6></div>",
        )

    def test_mixed_content(self):
        md = """
# Welcome

This is a paragraph with **bold** and _italic_.

> A wise quote
> spans multiple lines

## Features

- Feature one
- Feature two with `code`
- Feature three

1. First step
2. Second step
3. Third step

```
code block here
with multiple lines
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # This one tests that all block types work together
        self.assertIn("<h1>Welcome</h1>", html)
        self.assertIn("<blockquote>A wise quote spans multiple lines</blockquote>", html)
        self.assertIn("<ul>", html)
        self.assertIn("<ol>", html)
        self.assertIn("<pre><code>", html)


# KNOWN LIMITATION
#     def test_nested_inline_markdown(self):
#         md = """
# This paragraph has **bold with _italic inside_** and `code with **bold**`.
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         # Test that inline markdown is properly parsed
#         self.assertIn("<b>bold with <i>italic inside</i></b>", html)

    def test_empty_list_items(self):
        md = """
- First item
- Second item
- Third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First item</li><li>Second item</li><li>Third item</li></ul></div>",
        )


    def test_multiline_quote(self):
        md = """
> This is line one
> This is line two
> This is line three with **bold**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is line one This is line two This is line three with <b>bold</b></blockquote></div>",
        )

    def test_code_preserves_markdown(self):
        md = """
```
def hello():
# This is a comment
print("**not bold**")
return `not code`
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # Verify that markdown syntax is NOT parsed inside code blocks
        self.assertIn("**not bold**", html)
        self.assertIn("`not code`", html)
        self.assertNotIn("<b>", html)

