import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_args(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), "<a href='https://www.google.com'>Click me!</a>")

        node3 = LeafNode("p", "")
        
        with self.assertRaises(ValueError): 
            node3.to_html()
