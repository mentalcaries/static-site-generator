from textnode import TextType, TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []

    for node in old_nodes:

        # if node.text__type is not TextType.TEXT
        if node.text__type != TextType.TEXT:
            split_nodes.append(node)
            continue
        # check if delimiter in node.text
        while delimiter in node.text:
            normal_text, start_delimited_text = node.text.split(delimiter, 1)
            split_nodes.append(TextNode(normal_text, TextType.TEXT))

            if delimiter not in start_delimited_text:
                raise Exception("Invalid Markdown Syntax")
            delimited_text, remaining_text = start_delimited_text.split(delimiter, 1)
            split_nodes.append(TextNode(delimited_text, text_type))
            node.text = remaining_text

        if node.text:
            split_nodes.append(TextNode(node.text, TextType.TEXT))
    return split_nodes


def extract_markdown_images(text):
    regex = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex, text)
    return matches


def extract_markdown_links(text):
    regex = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex, text)
    return matches


def split_nodes_image(old_nodes):
    split_nodes = []

    for node in old_nodes:
        if node.text__type != TextType.TEXT:
            split_nodes.append(node)
            continue
        node_text = node.text
        extracted_images = extract_markdown_images(node_text)
        if len(extracted_images) == 0:
            split_nodes.append(node)
            continue
        for extracted_image in extracted_images:
            alt, url = extracted_image

            image_string = f"![{alt}]({url})"
            plain_text, remaining_text = node_text.split(image_string, 1)

            if plain_text != "":
                split_nodes.append(TextNode(plain_text, TextType.TEXT))
            split_nodes.append(TextNode(alt, TextType.IMAGE, url))
            node_text = remaining_text
        if node_text != "":
            split_nodes.append(TextNode(node_text, TextType.TEXT))

    return split_nodes


def split_nodes_link(old_nodes):
    split_nodes = []

    if len(old_nodes) == 0:
        raise Exception("Invalid input")

    for node in old_nodes:
        if node.text__type !=  TextType.TEXT:
            split_nodes.append(node)
            continue
        node_text = node.text
        extracted_links = extract_markdown_links(node_text)
        if len(extracted_links) == 0:
            split_nodes.append(node)
            continue
        for extracted_link in extracted_links:
            anchor, url = extracted_link

            link_string = f"[{anchor}]({url})"
            plain_text, remaining_text = node_text.split(link_string, 1)

            if plain_text != "":
                split_nodes.append(TextNode(plain_text, TextType.TEXT))
            split_nodes.append(TextNode(anchor, TextType.LINK, url))
            node_text = remaining_text
        if node_text != "":
            split_nodes.append(TextNode(node_text, TextType.TEXT))

    return split_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)

    images = split_nodes_image([node])
    links = split_nodes_link(images)
    bold = split_nodes_delimiter(links, "**", TextType.BOLD)
    italics = split_nodes_delimiter(bold, "*", TextType.ITALIC)
    code = split_nodes_delimiter(italics, "`", TextType.CODE)
    
    return code

