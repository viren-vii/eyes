# 🎯 Voice-Enabled Browser Assistant for Visually Impaired Users

This project implements an AI-powered browser assistant specifically designed to help visually impaired users navigate and interact with web content through voice commands and audio feedback.

## ✨ Features

- **Voice Input**: Uses speech recognition to capture user commands and queries
- **Audio Feedback**: Converts text responses to speech for a hands-free experience
- **Intelligent Navigation**: AI-powered assistance for browsing websites
- **Context-Aware**: Understands and remembers context during the browsing session

## 🛠️ Core Components

### 1. 🎤 Voice Interface
- Speech-to-Text using Google Speech Recognition
- Text-to-Speech for audio feedback
- Automatic silence detection for natural conversation flow

### 2. 🧠 AI Agent
- Powered by GPT-4 for natural language understanding
- Contextual awareness of browser state and user needs
- Intelligent decision-making for navigation and interaction

### 3. 🌐 Browser Control
- Automated browser interaction and navigation
- Page content analysis and summarization
- Form filling and button clicking capabilities

## 🚀 Getting Started

### Installation

1. Clone the repository
2. Create a `.env` file in root directory and add `OPENAI_API_KEY` to it.
3. If you don't have `uv` installed, install it using [this](https://docs.astral.sh/uv/getting-started/installation/#installation-methods).
4. Install dependencies (root directory): 
   ```bash
   uv pip install .
   ```
5. Run the application: 
   ```bash
   uv run dev
   ```

### Usage

- Start the application
- Use voice commands to navigate and interact with the browser
- Enjoy the hands-free browsing experience!
