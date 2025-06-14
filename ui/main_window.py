# ui/main_window.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit,
    QPushButton, QTreeWidget, QTreeWidgetItem
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from app.controller import MindMapController



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MindMap Decoder")

        self.controller = MindMapController()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.title = QLabel("🧠 MindMap Decoder")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        
        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Enter your thought or goal here...")

        self.run_button = QPushButton("Decode My Mind")
        self.run_button.clicked.connect(self.run_decoder)

        self.tree_view = QTreeWidget()
        self.tree_view.setHeaderHidden(True)
        
        self.title.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        self.title.setStyleSheet("color: #334155; margin-bottom: 15px;")

        # Style input box:
        self.input_box.setStyleSheet("""
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 8px;
            font-size: 14px;
            font-family: 'Segoe UI';
        """)

        # Style button with hover effect:
        self.run_button.setStyleSheet("""
            background-color: #3b82f6;
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 15px;
            font-family: 'Segoe UI';
        """)
        self.run_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.run_button.setAutoDefault(False)
        self.run_button.setDefault(False)

        # Add hover using event filter (optional, else basic style works fine)
        # For now, simple static color is fine

        # Style tree widget:
        self.tree_view.setStyleSheet("""
            border: none;
            font-size: 14px;
            font-family: 'Segoe UI';
            color: white;
        """)

        layout.addWidget(self.title)
        layout.addWidget(self.input_box)
        layout.addWidget(self.run_button)
        layout.addWidget(self.tree_view)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(12)

        self.setLayout(layout)
        self.resize(600, 500)

    def run_decoder(self):
        user_input = self.input_box.toPlainText()
        if not user_input.strip():
            return

        self.controller.process_input(user_input)
        self.display_tree()

    def display_tree(self):
        self.tree_view.clear()
        root_node = self.controller.thought_map.root
        root = QTreeWidgetItem([str(root_node.content)])
        self.tree_view.addTopLevelItem(root)

        def add_children(ui_node, logic_node):
            for child in logic_node.children:
                text = child.content["text"] if isinstance(child.content, dict) and "text" in child.content else str(child.content)
                ui_child = QTreeWidgetItem([text])
                # ui_child = QTreeWidgetItem([child.content])
                ui_node.addChild(ui_child)
                add_children(ui_child, child)

        add_children(root, root_node)
        self.tree_view.expandAll()

