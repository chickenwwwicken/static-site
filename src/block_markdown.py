
def markdown_to_blocks(markdown):
    blocks_raw = markdown.split("\n\n")
    blocks = []
    for block in blocks_raw:
        block = block.strip()
        if block == "":
            continue
        blocks.append(block)
    return blocks

