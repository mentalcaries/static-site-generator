from textnode import TextType, TextNode



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
