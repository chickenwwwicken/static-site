from textnode import TextNode, TextType

def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:

        # node is not a text type
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        
        # node is text type 
        if delimeter in text:
            split_text = node.text.split(delimeter)
            if len split text

    


