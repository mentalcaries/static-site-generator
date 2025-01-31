import re
from textnode import text_node_to_html_node
from utils import text_to_textnodes
from htmlnode import LeafNode, ParentNode


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

    if re.match(r"^```[\S\s]*?```$", block):
        return "code"

    if re.match(r"^>.*", block):
        return "blockquote"

    if re.match(r"^\* .*|- .*", block):
        return "unordered_list"
    
    if re.match(r"\d\. ", block):
        return "ordered_list"
    return "paragraph"


def text_to_children(text):
    # return a list of HTML Nodes that represent the inline markdown
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type: 
        # create new HTML node based on block type. 
            case "heading":
                return create_heading_node(block)
            case "code":
                return create_code_node(block)
            case "unordered_list":
                return create_unordered_list_node(block)
            case "ordered_list":
                return create_ordered_list_node(block)
            case "blockquote":
                return create_blockquote_node(block)
            case "paragraph":
                return create_paragraph_node(block)    


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for markdown_block in markdown_blocks:
        html_node = block_to_html_node(markdown_block)
        html_nodes.append(html_node)
    
    return ParentNode("div", html_nodes, None)
        # assign proper HTML node objets to block node

def text_to_children(text):
    # return a list of HTML Nodes that represent the inline markdown
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes


def create_heading_node(text):
    if not text.startswith("#"):
        raise Exception("Invalid heading)")
    heading = re.match(r"^(#{1,6}) ", text)
    if not heading:
        raise Exception("Invalid heading format")
    heading_level = len(heading.group(1))
    children = text_to_children(text[heading.end() :].strip())
    return ParentNode(f"h{heading_level}", children)


def create_code_node(text):
    code = re.match(r"^```([\s\S]*?)```$", text.strip())
    if not code:
        raise Exception("Invalid code block")
    code_content = text_to_children(code.group(1).strip())
    return ParentNode("code", code_content)


def create_unordered_list_node(text):

    list = text.strip().split("\n")
    list_items = []

    for list_item in list:

        list = re.match(r"^[-*]\s+(.*)", list_item)
        if not list:
            raise Exception("Invalid list")
        children = text_to_children(list.group(1).strip())
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)


def create_ordered_list_node(text):

    list = text.strip().split("\n")
    list_items = []

    for list_item in list:
        list = re.match(r"^\d+[.)]\s+(.*)", list_item)
        if not list:
            raise Exception("Invalid List Item")
        children = text_to_children(list.group(1).strip())
        list_items.append(ParentNode("li", children))

    return ParentNode("ol", list_items)


def create_paragraph_node(text):
    lines = text.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def create_blockquote_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def extract_title(markdown):
    if not markdown.startswith('# '):
        raise Exception('Invalid header')
    return markdown.lstrip('# ')