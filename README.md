# X Posting Bot

This project is a lightweight AI-powered bot that automatically generates and posts content to X (formerly Twitter) using a quantized LLM and the X API. It is designed for efficient local execution and easy deployment.

## Features
- **AI-Powered Content Generation:** Uses a quantized Mistral model to generate relevant tweets based on input text.
- **Automated Posting:** Outlined integration for the X API using Tweepy to post tweets programmatically (requires elevated account).
- **Efficient Local Execution:** Runs on a lightweight model with minimal system requirements.

## Tech Stack
- **Python** (Primary language)
- **Tweepy** (X API integration)
- **Llama.cpp / Hugging Face Transformers** (LLM inference)
- **Dotenv** (Environment variable management)

## Setup & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/sameagol/xposting.git
   cd xposting
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up API keys (store in a `.env` file):
   ```
   X_CONSUMER_KEY=your_api_key
   X_CONSUMER_SECRET=your_api_secret
   X_ACCESS_TOKEN=your_access_token
   X_ACCESS_TOKEN_SECRET=your_access_token_secret
   ```
4. Run the bot:
   ```sh
   python llm.py
   ```

## Status
✅ **Core functionality implemented:** LLM-based content generation + X API posting.
🚀 **Next steps:** Prompt refinement, Robust integration, Scheduling, and Resource optimizaiton.

## Contact
Samuel Freda  
GitHub: [sameagol](https://github.com/sameagol)  
Email: samuel.e.freda@gmail.com
