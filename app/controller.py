# app/controller.py

from core.text_processor import TextProcessor
from core.reasoning_engine import ReasoningEngine
from core.thought_map import ThoughtMap

class MindMapController:
    def __init__(self):
        self.text_processor = TextProcessor()
        self.reasoning_engine = ReasoningEngine()
        self.thought_map = None

    def process_input(self, user_input: str):
        cleaned = self.text_processor.clean_text(user_input)
        subthoughts = self.reasoning_engine.generate_sub_thoughts(cleaned)
        self.thought_map = ThoughtMap(user_input, subthoughts)

    def display_map(self):
        if self.thought_map:
            self.thought_map.traverse()
        else:
            print("No mindmap to display yet.")
