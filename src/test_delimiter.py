from utils import split_nodes_delimiter
import unittest
from textnode import TextNode, TextType


class TestDelimiter(unittest.TestCase):

    def test_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

        node_2 = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes_2 = split_nodes_delimiter([node_2], "**", TextType.BOLD)

        self.assertEqual(
            new_nodes_2,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()
