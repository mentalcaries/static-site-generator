import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises( NotImplementedError, node.to_html)

    def test_props_attributes(self):
        node = HTMLNode("a", "", None, { "href": "https://jaggernauth.dev"})

        self.assertEqual(node.props_to_html(), " href='https://jaggernauth.dev'")

    def test_no_attributes(self):
        node = HTMLNode(None, None, None, None,)
        self.assertEqual(node.props_to_html(), "")


    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTML Node: tag: p, value: What a strange world, children: None, props: {'class': 'primary'}",
        )

if __name__ == "__main__":
    unittest.main()