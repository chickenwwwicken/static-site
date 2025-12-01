class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props={}):

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
            props_html += f'{prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
