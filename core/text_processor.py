import string

class TextProcessor:
    def __init__(self):
        # Simple stopwords list; can expand later
        self.stopwords = {"the", "is", "at", "which", "on", "and", "a", "an", "to", "for"}

    def clean_text(self, text: str) -> str:
        if not text or not isinstance(text, str):
            return ""

        # Lowercase
        text = text.lower().strip()

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Remove stopwords
        words = text.split()
        words = [word for word in words if word not in self.stopwords]

        # Join back
        cleaned_text = " ".join(words)
        return cleaned_text
