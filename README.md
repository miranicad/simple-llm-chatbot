# 🤖 Tamira AI - Portfolio Chatbot

An AI-powered chatbot built with Streamlit and OpenAI's GPT-4o-mini, designed to showcase my skills and projects on my portfolio website. This chatbot provides visitors with an interactive way to learn about my background, technical expertise, and experience.

## ✨ Features

- **Real-time AI responses** with streaming output
- **Custom terminal-style UI** with dark theme
- **Conversational memory** - maintains context throughout the chat
- **Intelligent prompt engineering** - responses are concise, direct, and informative
- **Responsive design** - works on desktop and mobile
- **Cost-efficient** - uses GPT-4o-mini for optimal performance/cost ratio

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **AI/ML**: OpenAI GPT-4o-mini API
- **Language**: Python 3.9+
- **Styling**: Custom CSS for terminal aesthetic
- **Environment Management**: python-dotenv

## 📁 Project Structure
```
simple-llm-chatbot/
├── .env                    # API keys and configuration (not in git)
├── .env.example           # Template for environment variables
├── .gitignore
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── config.py             # Configuration loader
├── prompt.py             # System prompt and AI instructions
├── styles.py             # Custom CSS styling
├── llm_client.py         # OpenAI API integration
└── app.py                # Main Streamlit application
```

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Setup

1. **Clone the repository**
```bash
   git clone https://github.com/yourusername/portfolio-chatbot.git
   cd portfolio-chatbot
```

2. **Create virtual environment**
```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
   cp .env.example .env
```
   
   Edit `.env` and add your OpenAI API key:
```
   OPENAI_API_KEY=sk-proj-your-key-here
   MODEL_NAME=gpt-4o-mini
   MAX_TOKENS=1024
   TEMPERATURE=0.3
```

5. **Run the application**
```bash
   streamlit run app.py
```

   The app will open in your browser at `http://localhost:8501`

## 📝 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `MODEL_NAME` | OpenAI model to use | `gpt-4o-mini` |
| `MAX_TOKENS` | Maximum response length | `1024` |
| `TEMPERATURE` | Response creativity (0-2) | `0.3` |

### Customizing the Prompt

Edit `prompt.py` to customize:
- Information about yourself
- Response style and tone
- Instructions for the AI assistant

### Styling

Modify `styles.py` to change:
- Color scheme
- Typography
- Layout and spacing
- Terminal aesthetic

## 💡 Key Learnings

Building this project taught me:

1. **LLM Integration**: Working with OpenAI's API, understanding token limits, streaming responses
2. **Prompt Engineering**: Crafting effective system prompts for consistent, high-quality responses
4. **State Management**: Handling conversation history in Streamlit's session state
5. **Best Practices**: Environment variable management, clean code structure, documentation


## 🎯 Future Enhancements

- [ ] Add RAG (Retrieval-Augmented Generation) for document-based responses
- [ ] Implement rate limiting for production deployment
- [ ] Add analytics to track popular questions
- [ ] Multi-language support (German, French, English)
- [ ] Integration with portfolio website projects


## 📄 License

Portfolio Viewing License
Copyright (c) 2026 Tamira Leber

PERMITTED ✅:
- View the source code on GitHub 
- Reference in discussions or educational contexts 
- Link to this repository

NOT PERMITTED ❌:
- Use, copy, or modify the code 
- Distribute or sublicense 
- Include in other projects 
- Commercial use of any kind

This code is provided solely for portfolio demonstration

## 👤 Author

**miranicad**

- Portfolio: [your-portfolio-url.com]
- LinkedIn: https://www.linkedin.com/in/tamira-leber-6a2101183/
- GitHub: https://github.com/miranicad]


**Built with ❤️ as part of my journey into AI/ML engineering**