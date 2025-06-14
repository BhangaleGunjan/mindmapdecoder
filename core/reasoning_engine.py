import ollama
import json
import re
import ast

class ReasoningEngine:
    def __init__(self, model="mistral"):
        self.model = model

    def generate_sub_thoughts(self, cleaned_text: str) -> dict:
        prompt = f"""
        🔧 Prompt Title:
            "Trace My Thought Process: Subthought Generator"

            🧠 Prompt:
            You are a cognitive reasoning assistant trained in introspective analysis and human thought deconstruction. Your task is to break down a final thought into its underlying subthoughts, assumptions, feelings, experiences, or micro-decisions that may have contributed to it.

            Act like a psychologist meets detective: infer context, deduce emotional and logical pathways, and present a step-by-step chain of thoughts that could realistically lead someone to arrive at the final thought.

            If necessary, speculate responsibly based on human behavior patterns and psychology.

            Input Format: I want to move to Japan.
            
            Output Format: 
            Subthoughts:
            1. "I’ve always been drawn to Japanese culture and values."
            3. "My current environment feels stagnant—I need a bigger challenge."
            4. "Living abroad could help me grow emotionally and professionally."
            5. "I’ve dreamed about Japan for years; maybe it’s time to chase that dream."
            6. "I don’t want to regret not taking bold steps when I had the chance."
            
            Heres the Input:
            "{cleaned_text}"

            Return ONLY the JSON array.
        """


        response = ollama.chat(model=self.model, messages=[
            {"role": "user", "content": prompt}
        ])

        content = response['message']['content']

        # First, try safe JSON parse
        try:
            thoughts = json.loads(response.message.content.strip())
            if not isinstance(thoughts, list):
                raise ValueError("Expected a list of sub-thoughts.")
            return thoughts

        # If that fails, try to extract valid-looking block with regex
        except json.JSONDecodeError:
            print("⚠️ JSON parsing failed. Attempting recovery...")
            return []