import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2= TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a URL", TextType.LINK)
        self.assertEqual(node.url, None)

    def test_eq_url(self):
        node = TextNode("this is a text node", TextType.ITALIC, "https://jaggernauth.dev")
        node2 = TextNode("this is a text node", TextType.ITALIC, "https://jaggernauth.dev")
        self.assertEqual(node, node2)

    def test_node_to_html(self):
        text_node_1 = TextNode("Test Heading 1", TextType.TEXT)
        text_node_2 = TextNode("BOLD TEXT", TextType.BOLD)
        text_node_3 = TextNode("CNet", TextType.LINK, "https://cnet.com")


        self.assertEqual(text_node_to_html_node(text_node_1).to_html(), "Test Heading 1")
        self.assertEqual(text_node_to_html_node(text_node_2).to_html(), "<b>BOLD TEXT</b>")
        self.assertEqual(text_node_to_html_node(text_node_3).to_html(), "<a href='https://cnet.com'>CNet</a>")


if __name__ == "__main__":
    unittest.main()