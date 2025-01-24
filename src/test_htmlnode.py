
from htmlnode import HTMLNode

# ------------------------------------------------------------------------------
# HTMLNode TESTS
def test_props_to_html():

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
    print(other_node)
    assert other_node.props_to_html() == ' class="button" id="submit"'


    # Test case 4: complex Node with all args
    child = HTMLNode(tag="span", value="world")
    node2 = HTMLNode(
        tag="div",
        children=[child],
        props={"class": "container"}
    )
    print(node2)



# -----------------------------------------------------------------------------------
# LeafNode TESTS
# Test case 1: Basic Leaf

def test_basic_leaf():
    basic_leafnode = LeafNode(tag="h1", value="Hellow")
    assert basic_leafnode.to_html() == "<h1>Hellow</h1>"

    
# Test case 2: leaf node with props

def test_node_w_props():
    test_props = {"href": "https://www.google.com", "target": "_blank"}
    leaf_w_props = LeafNode(tag="a", value="google", props=test_props)
    assert leaf_w_props.to_html() == '<a href="https://www.google.com" target="_blank">google</a>'


# Test case 3: leaf with no tag

def test_w_no_tag():
    leaf_no_tag = LeafNode(value="google")
    assert leaf_no_tag.to_html() == 'google'

# Test case 4: Error , no value
# Using pytest to check for ValueError instead of assert 

def test_no_value():
    try:
        leaf_no_value = LeafNode(tag="div", props={"class": "test"}, value=None)
        leaf_no_value.to_html()
        assert False, "Expected ValueError was not raised"
    except ValueError:
        pass



# ------------------------------------------------------------------------
# ParentNode Tests
# Test case 1: Single parent, Single Child 
def test_singlep_singlec():
    parent = ParentNode("div", children=[LeafNode("p", "Hello, world!")])
    assert parent.to_html() == "<div><p>Hello, world!</p></div>" 

# Test case 2: Nested Parents
def test_nestedp():
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
    try:
        node = ParentNode(None, children=[])
        node.to_html()
    except ValueError as e:
        assert str(e) == "All Parent Nodes must have tag"


# Test case 4: No Children
def test_no_children():
    try:
        node = ParentNode("div", children=[])
        node.to_html()
    except ValueError as e:
        assert str(e) == "U missin ur children boy"



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
    print("All tests passed!")
