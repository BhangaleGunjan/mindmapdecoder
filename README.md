# 🧠 MindMapDecoder

**MindMap Decoder** is a modular, scalable Python project that transforms user thoughts, goals, or abstract ideas into a visual mind map using reasoning and logic. It's designed to help users clarify their intentions, break down complex goals, and visualize mental models.

---

## 🚀 Features

- 🧩 Modular architecture for easy customization and scaling
- 🔍 Natural language input processing
- 🌳 Tree structure generation for ideas/goals
- 🧠 Basic reasoning logic to generate meaningful branches
- 📦 Easy to extend with your own AI/logic modules
- 🎨 Planned support for mind map visualization

## 🔧 Requirements

  - Python 3.10+
  - Ollama installed and running locally
  - Mistral model pulled via Ollama

### 📥 Setting up Ollama + Mistral

Install Ollama:
  - Follow the official install instructions: https://ollama.com/download

Pull the Mistral model:
  - `ollama pull mistral`

Verify it's running:
  - `ollama run mistral`
    
You should see a prompt indicating that Mistral is active and listening for input.

## 🛠️ Installation

1. Clone the repo:
  - `git clone https://github.com/your-username/mindmap-decoder.git`
  - `cd mindmap-decoder`

3. Set up a virtual environment (recommended):
  - `python -m venv venv`
  - `source venv/bin/activate`
  - On Windows use: `venv\Scripts\activate`
    
4. Install dependencies:
  - `pip install -r requirements.txt`

## ⚙️ Usage

Run the main script:
  - `python main.py`

You’ll be prompted to enter a goal, thought, or abstract idea. The script will process the input, apply logic to expand it into a tree-like structure, and then display the result in a textual format.

### Usage

<p align="center">
  <img src="Screenshot 2025-06-14 130324.png" width="500"/>
</p>


© 2025 Gunjan Bhangale. All Rights Reserved. 
