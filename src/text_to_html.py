from htmlnode import HTMLNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType
from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from inline_markdown import text_to_textnodes



def markdown_to_html_node(markdown):
    html_nodes = []

    # split the markdown into blocks
    split_md = markdown_to_blocks(markdown)

    # loop over each block and get block type
    for block in split_md:
        block_type = block_to_block_type(block)

        # split the block into lines
        split_block = block.split("\n")


        # ----------------------------------------------------------------------
        # -------------------------------------------------------PARAGRAPH-BLOCK
        if block_type == BlockType.PARAGRAPH:
            paragraph_text = []
            for line in split_block:
                line = line.lstrip()
                paragraph_text.append(line)
            paragraph_text = " ".join(paragraph_text)
            children = text_to_children(paragraph_text)
            html_nodes.append(ParentNode("p", children=children))

        # ----------------------------------------------------------------------
        # ---------------------------------------------------------HEADING-BLOCK
        if block_type == BlockType.HEADING:
            # h_index = block.find(" ")
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            h_text = block[level+1:].lstrip()
            h_children = text_to_children(h_text)
            html_nodes.append(ParentNode(f"h{level}", children=h_children))

        # ----------------------------------------------------------------------
        # -----------------------------------------------------------QUOTE-BLOCK
        if block_type == BlockType.QUOTE:
            quote_text = []
            for line in split_block:
                line = line[2:].lstrip()
                quote_text.append(line)
            quote_text = " ".join(quote_text)
            children = text_to_children(quote_text)
            html_nodes.append(ParentNode("blockquote", children=children))

        # ----------------------------------------------------------------------
        # --------------------------------------------------UNORDERED-LIST-BLOCK
        if block_type == BlockType.UNORDERED_LIST:
            list_children = []
            for line in split_block:
                if line.strip() != '':
                    line = line[2:].lstrip()
                    item_children = text_to_children(line)
                    list_children.append(ParentNode("li", children=item_children))
            html_nodes.append(ParentNode("ul", children=list_children))

        # ----------------------------------------------------------------------
        # ----------------------------------------------------ORDERED-LIST-BLOCK
        if block_type == BlockType.ORDERED_LIST:
            list_children = []
            for line in split_block:
                # any empty line is not added or worked with
                if line.strip() != '':
                    # find the dot in the "1. " to know where to slice
                    dot_index = line.find(".")
                    # slice off number and strip spaces
                    line = line[dot_index+1:].lstrip()
                    item_children = text_to_children(line)
                    list_children.append(ParentNode("li", children=item_children))
            html_nodes.append(ParentNode("ol", children=list_children))

        # ----------------------------------------------------------------------
        # ------------------------------------------------------------CODE-BLOCK
        if block_type == BlockType.CODE:
            # removes first and last line
            code_lines = split_block[1:-1]
            # join text with /n and then adds another newline at the end
            # original markdown code block includes newlines at the end.
            code_text = "\n".join(code_lines) + "\n"

            # create the htmlnode (add the <code> tag)
            code_text_node = TextNode(code_text, TextType.CODE)
            code_html_node = text_node_to_html_node(code_text_node)

            # add the <pre> tag
            pre_node = ParentNode("pre", children=[code_html_node])
            html_nodes.append(pre_node)


    return ParentNode("div", children=html_nodes)



def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children




















