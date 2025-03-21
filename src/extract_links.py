import re

def extract_markdown_images(text):
    # This will directly return the list of tuples+ from re.findall
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    # This will directly return the match results
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
