
from htmlnode import HTMLNode, LeafNode, ParentNode

# ------------------------------------------------------------------------------
# HTMLNode TESTS

def test_props_to_html():
    print("---running HTMLNode Tests...---")
    print("running test_props_to_html...")
    # Test case 1: Node with props
    test_props = {
        "href": "https://www.google.com",
        "target": "_blank"
    }
    node = HTMLNode(props=test_props)
    assert node.props_to_html() == ' href="https://www.google.com" target="_blank"'


    # Test case 2: Node with empty props
    empty_node = HTMLNode()
    assert empty_node.props_to_html() == ''


    # Test case 3: Node with different props
    other_props = {
        "class": "button",
        "id": "submit"
    }
    other_node = HTMLNode(props=other_props)
    assert other_node.props_to_html() == ' class="button" id="submit"'

    print("--------------------------------")


# -----------------------------------------------------------------------------------
# LeafNode TESTS
# Test case 1: Basic Leaf

def test_basic_leaf():
    print("---running LeafNode Tests...---")
    print("running test_props_to_html...")
    basic_leafnode = LeafNode(tag="h1", value="Hellow")
    assert basic_leafnode.to_html() == "<h1>Hellow</h1>"

    
# Test case 2: leaf node with props

def test_node_w_props():
    print("running test_node_w_props...")
    test_props = {"href": "https://www.google.com", "target": "_blank"}
    leaf_w_props = LeafNode(tag="a", value="google", props=test_props)
    # print('props:', leaf_w_props.props) 
    # print(leaf_w_props.to_html()) 
    assert leaf_w_props.to_html() == '<a href="https://www.google.com" target="_blank">google</a>'


# Test case 3: leaf with no tag

def test_w_no_tag():
    print("running test_w_no_tag...")
    leaf_no_tag = LeafNode(value="google")
    assert leaf_no_tag.to_html() == 'google'

# Test case 4: Error , no value
# Using pytest to check for ValueError instead of assert 

def test_no_value():
    print("running test_no_value...")
    try:
        leaf_no_value = LeafNode(tag="div", props={"class": "test"}, value=None)
        leaf_no_value.to_html()
        assert False, "Expected ValueError was not raised"
    except ValueError:
        pass

    print("--------------------------------")

# ------------------------------------------------------------------------
# ParentNode Tests
# Test case 1: Single parent, Single Child 
def test_singlep_singlec():
    print("---running ParentNode Tests...---")
    print("running test_singlep_singlec...")
    parent = ParentNode("div", children=[LeafNode("p", "Hello, world!")])
    assert parent.to_html() == "<div><p>Hello, world!</p></div>" 

# Test case 2: Nested Parents
def test_nestedp():
    print("running test_nestedp...")
    parent = ParentNode("div", children=[
        ParentNode("span", children=[
            LeafNode("b", "Bold text"),
        ]),
        LeafNode("i", "Italic text")
    ])
    assert parent.to_html() == "<div><span><b>Bold text</b></span><i>Italic text</i></div>"
    # Expected Output: <div><span><b>Bold text</b></span><i>Italic text</i></div>


# Test case 3: Missing Tag
def test_missing_tag():
    print("running test_missing_tag...")
    try:
        node = ParentNode(None, children=[])
        node.to_html()
    except ValueError as e:
        assert str(e) == "All Parent Nodes must have tag"


# Test case 4: No Children
def test_no_children():
    print("running test_no_children...")
    try:
        node = ParentNode("div", children=[])
        node.to_html()
    except ValueError as e:
        assert str(e) == "Parent Nodes must have children"

    print("--------------------------------")

# ------------------------------------------------------------------------
# Complex Node Tests
# Test case 1: Complex Nesting 1 
def test_complex_nesting1():
    print("---running Complex Node Tests...---")
    print("running test_complex_nesting1...")

    # create all leaf nodes
    hello_node = LeafNode(None, "Hello ")
    bold_node = LeafNode("b", "bold")
    world_node = LeafNode(None, " world!")

    italic_node_props = {"class": "emphasis"}
    italic_node = LeafNode("i", "This is italic", props=italic_node_props)

    # create all parent nodes
    paragraph_node = ParentNode("p", [hello_node, bold_node, world_node, italic_node])
    
    div_node_props = {"class": "container"}
    div_node = ParentNode("div", [paragraph_node], div_node_props)

    # print("div_node.to_html():", div_node.to_html())
    assert div_node.to_html() == '<div class="container"><p>Hello <b>bold</b> world!<i class="emphasis">This is italic</i></p></div>'



# ------------------------------------------------------------------------
# calling all functions

if __name__ == '__main__':
    # Run the HTMLNode tests
    test_props_to_html()
    # Run the LeafNode tests
    test_basic_leaf()
    test_node_w_props()
    test_w_no_tag()
    test_no_value()
    # Run the ParentNode tests
    test_singlep_singlec()
    test_nestedp()
    test_missing_tag()
    test_no_children()
    # Run the complex node tests
    test_complex_nesting1()
    print("All tests passed!")
