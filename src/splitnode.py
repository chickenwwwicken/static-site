import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:

        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        result_nodes = []

        # Keep processing the text until no more delimeters are found
        while delimiter in text:
            # find the opening delimiter
            split_text = text.split(delimiter, 1)
            if len(split_text) < 2:
                break

            # Text before the delimiter and remaining
            before_delimiter = split_text[0]
            remaining_text = split_text[1]

            # Find the closing delimiter
            if delimiter not in remaining_text:
                raise Exception(f"Invalid Markdown syntax: No closing delimiter found")

            # Split at the clsing delimiter
            split_remaining = remaining_text.split(delimiter, 1)
            delimited_text = split_remaining[0] # Text between delimiters
            after_delimiter = split_remaining[1] # Text after the closing delimiter
            # add nodes for text before and inside delimiters
            if before_delimiter:
                result_nodes.append(TextNode(before_delimiter, TextType.NORMAL))
            if delimited_text:
                result_nodes.append(TextNode(delimited_text, text_type))

            # Update text to continue processing
            text = after_delimiter

        # Add any remaining text
        if text: 
            result_nodes.append(TextNode(text, TextType.NORMAL))

        # Add all processed nodes from this old_node to new_nodes
        new_nodes.extend(result_nodes)

    # Return the complete list     
    return new_nodes

# -----------------------------------------------------------------------------
# 3.4 Extracting links from images and regular links

def extract_markdown_images(text):
    # This will directly return the list of tuples+ from re.findall
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    # This will directly return the match results
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

# -----------------------------------------------------------------------------
# 3.5 Split Images and links

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if extract_markdown_images(old_node) == 
        extracted = extract_markdown_images(old_node)
        


def split_nodes_link(old_nodes):
     
