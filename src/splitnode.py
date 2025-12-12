import re
from textnode import TextType, TextNode

# ---------------------------------------------------------
# -------------------bold-italic-code----------------------
# ---------------------------------------------------------

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # if node is not Text
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            # move to the next node
            continue

        # if there's no delimiter
        if delimiter not in old_node.text:
            new_nodes.append(old_node)
            # move to the next node
            continue

        # create the parts list:
        parts = old_node.text.split(delimiter)

        # if there is no closing delimiter
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown Syntax: No closing {delimiter}")

        # if there is delimiter
        for i, part in enumerate(parts):
            # we skip the empty strings so that our logic works even if node starts w delimiter
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes



# ---------------------------------------------------------
# -------------------links-images--------------------------
# ---------------------------------------------------------


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # if node is not Text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            # move to the next node
            continue

        # extract images
        ext_image = extract_markdown_images(node.text)

        # if no images...
        if not ext_image:
            new_nodes.append(node)
            continue

        current_text = node.text

        # each image (tuple) we name (alt, url) in the for loop
        for alt, url in ext_image:
            # use the markdown image as delimiter
            parts = current_text.split(f"![{alt}]({url})", 1)
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            current_text = parts[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # if node is not Text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            # move to the next node
            continue

        # extract links
        ext_link = extract_markdown_links(node.text)

        # if no link...
        if not ext_link:
            new_nodes.append(node)
            continue

        current_text = node.text

        # each link (tuple) we name (link, url) in the for loop
        for link, url in ext_link:
            # use the markdown link as delimiter
            parts = current_text.split(f"[{link}]({url})", 1)
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(link, TextType.LINK, url))
            current_text = parts[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes



