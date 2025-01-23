import re


def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    stripped_blocks = []
    for split_block in split_blocks:
        stripped_block = split_block.strip()
        if stripped_block != "":
            stripped_blocks.append(stripped_block)
    return stripped_blocks


def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return "heading"

    if re.match(r"^```[\S\s]*?``$", block):
        return "code"

    if re.match(r"^>.*", block):
        return "quote"

    if re.match(r"^\* .*|- .*", block):
        return "unordered_list"
    
    if re.match(r"\d\. ", block):
        return "ordered_list"
    return "paragraph"
