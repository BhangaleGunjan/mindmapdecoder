# core/thought_map.py

from core.node import Node

class ThoughtMap:
    def __init__(self, root_text: str, subthoughts: dict):
        self.root = Node(root_text, category="root")
        self.build_tree(subthoughts)

    def build_tree(self, subthoughts: dict):
        for thought in subthoughts:
            self.root.add_child(Node(thought, category="thought"))

    def traverse(self, node: Node = None, depth=0):
        if node is None:
            node = self.root
        indent = "  " * depth
        print(f"{indent}- {node.content} ({node.category})")
        for child in node.children:
            self.traverse(child, depth + 1)
