# core/node.py

class Node:
    def __init__(self, content: str, category: str = "root"):
        self.content = content
        self.category = category
        self.children = []

    def add_child(self, node: 'Node'):
        self.children.append(node)

    def __repr__(self):
        return f"Node({self.content}, {self.category}, {len(self.children)} children)"
