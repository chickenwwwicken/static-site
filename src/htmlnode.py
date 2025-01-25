class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html = ''
        if self.props == None:
            return html
        for prop in self.props:
            html += f' {prop}="{self.props[prop]}"'
        return html

    def __repr__(self):
        return f'tag: {self.tag} \nvalue: {self.value} \nchildren: {self.children} \nprops: {self.props}'


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        # props_str = ''
        if not self.value:
            raise ValueError('All Leaf Nodes must have value')
        if not self.tag:
            return f'{self.value}'
        props_str = self.props_to_html() if self.props else ''
        return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        # validate 
        if not self.tag:
            raise ValueError('All Parent Nodes must have tag')
        if not self.children:
            raise ValueError('Parent Nodes must have children')
        
        # wrap the children in parent tags
        # also w the logic of add props if necessary to initial parent tag...
        # full_html = f"<{self.tag}>"
        # props_str = ''

        props_str = self.props_to_html() if self.props else ''
        full_html = f'<{self.tag}{props_str}>'

        for child in self.children:
            # check if parent of leaf
            if isinstance(child, ParentNode): # Recursive case
                full_html += child.to_html()
            elif isinstance(child, LeafNode): # Base Case
                full_html += child.to_html()

        # close the children in parent tags
        full_html += f"</{self.tag}>"
        return full_html

