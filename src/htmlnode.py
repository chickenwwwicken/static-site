from textnode import TextType

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):

        # htmlnode without tag will just render as raw text
        # tag = tag name e.g. "p", "a", "h1"
        self.tag = tag

        # htmlnode without value will be assumed to have children
        # value = a string representing the value of the html tag
        self.value = value

        # htmlnode without children will be assumed to have value
        # children = list of htmlnode objects that are inside this node
        self.children = children

        # htmlnode without props simply won't have any attributes
        # props = dict of key-value pairs, representing attributes of htmltag
        # e.g. link <a> tag might have {"href": "https://..."} prop
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f" {prop}='{self.props[prop]}'"
        return props_html

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have value")

        if self.tag == None:
            return self.value

        props_str = self.props_to_html()
        html_tag = f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        return html_tag

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

def __repr__(self):
    return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


# -----------------
# TEXT to HTML func
# -----------------

def text_node_to_html_node(text_node):

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode('b', text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text)

    if text_node.text_type == TextType.LINK:
        return LeafNode('a', text_node.text, {'href': text_node.url})

    if text_node.text_type == TextType.IMAGE:
        return LeafNode('img', None, {'src': text_node.url, 'alt': text_node.text})

    raise Exception("Invalid type of TextNode")

