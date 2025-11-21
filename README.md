# Mr Vivian's Business Intelligence Assistant

An AI-powered chatbot I built to help business analysts create reports, understand metrics, and get business intelligence guidance - completely free using Ollama.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)

## Why I Built This

As a business analyst, I was spending 4-6 hours on tasks that should take 30 minutes. I built this to solve my own daily problem - constantly switching between tools, Googling metric definitions, and figuring out report structures.

**Before:** 4-6 hours per report  
**After:** 1.5-2 hours per report

It's now part of my daily workflow and saves me hours every week. No API keys needed - uses Ollama (free, local AI) so it works completely offline.

## What It Does

- Generates report outlines in seconds
- Explains business metrics with formulas and examples
- Provides data analysis guidance
- Creates presentation structures
- Answers business intelligence questions in plain English

## Screenshots

### Main Interface
![Main Interface](Screenshots/Assistant%20Interface.jpeg)

### Example Usage - Asking a Question
![Asking a Question](Screenshots/Business%20Assistant%20Queried.png)

### Loading State
![Thinking](Screenshots/Business%20Assistant%20thinking%20about%20query.png)

### Example Response - Churn Rate Explanation
![Churn Rate Explanation](Screenshots/Result%20of%20Query%20on%20Churn%20Rate.png)

## Quick Start

### Step 1: Install Python
Make sure you have Python 3.8 or higher installed.
- Download from: https://www.python.org/downloads/
- During installation, check "Add Python to PATH"

### Step 2: Install Ollama
Download and install Ollama (the free AI engine):
- **Windows/Mac/Linux:** https://ollama.ai
- Just download and install - no configuration needed!

### Step 3: Download the Model
Open your terminal/command prompt and run:
```bash
ollama pull llama3
```
This downloads the AI model (takes 2-5 minutes, only needed once).

### Step 4: Install Python Dependencies
1. Open terminal/command prompt
2. Navigate to the project folder:
   ```bash
   cd bi-assistant
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Step 5: Run the Application
```bash
python app_ollama.py
```

You should see:
```
Starting Flask application...
Open http://localhost:5000 in your browser
```

### Step 6: Open in Browser
**Open your web browser and go to:**
```
http://localhost:5000
```

**That's it!** You should see the chat interface. Start asking questions!

## How to Use

### Basic Usage
1. Type your question in the input box at the bottom
2. Press Enter or click "Send"
3. Wait for response (usually 10-30 seconds)
4. Read the answer - it's formatted and ready to use!

### Example Questions

**Report Generation:**
```
"Create a quarterly sales report outline"
"Help me create a presentation about Q4 performance"
"Generate a customer analysis report structure"
```

**Metric Explanations:**
```
"What is customer churn rate and how do I calculate it?"
"Explain revenue vs profit in simple terms"
"What does ROI mean in business?"
```

**Analysis Guidance:**
```
"I have sales data for 2024, what should I analyze?"
"What metrics should I track for customer retention?"
"Help me plan an analysis of our marketing campaigns"
```

**Presentation Help:**
```
"Help me create a presentation about our Q4 performance for the board meeting"
"I need to explain why sales increased 15%, create a presentation structure"
```

## Accessing the Application

Once the application is running, access it at:

### **http://localhost:5000**

**What is localhost?**
- `localhost` = your own computer
- `5000` = the port number where the app runs
- Just type this address in any web browser (Chrome, Firefox, Edge, etc.)

**Important:** The application must be running (Step 5) for the website to work!

## Project Structure

```
bi-assistant/
├── app_ollama.py          # Main application
├── templates/
│   └── index.html         # Web interface
├── prompts/               # AI prompt templates
│   ├── report_generation.txt
│   ├── metric_explanation.txt
│   └── analysis_guidance.txt
├── static/
│   └── logo.png          # Your logo (optional)
├── requirements.txt       # Python dependencies
├── .env                   # Configuration (auto-created)
└── README.md             # This file
```

## Troubleshooting

### "python is not recognised"
- Python is not installed or not in PATH
- Reinstall Python and make sure to check "Add Python to PATH"
- Or try: `python3` instead of `python`

### "Cannot connect to Ollama"
1. Make sure Ollama is installed (Step 2)
2. Check if Ollama is running:
   ```bash
   ollama list
   ```
   If this works, Ollama is running.

### "Model not found"
```bash
ollama pull llama3
```
Wait for it to download.

### "Module not found" or "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### "Port 5000 already in use"
- Another application is using port 5000
- Close other applications
- Or restart your computer

### Browser shows "This site can't be reached"
1. Make sure the application is running (check terminal window)
2. Check the URL: `http://localhost:5000` (not `https://`)
3. Try: `http://127.0.0.1:5000` instead
4. Make sure you didn't close the terminal window

## Quick Reference

**Starting the App:**
```bash
cd bi-assistant
python app_ollama.py
```
Then open: http://localhost:5000

**Common Questions:**
- "Create a [type] report outline"
- "What is [metric] and how do I calculate it?"
- "I have [data], what should I analyze?"
- "Help me create a presentation about [topic]"

**Stop the Application:**
- Press `Ctrl + C` in the terminal window

## Summary

**To run the website:**
1. Python installed
2. Ollama installed
3. Model downloaded (`ollama pull llama3`)
4. Dependencies installed (`pip install -r requirements.txt`)
5. Application running (`python app_ollama.py`)
6. Browser open at `http://localhost:5000`

**That's it!** You're ready to use the Business Intelligence Assistant!

## License

This project is open source and available for portfolio use.

## Author

**Vivian Ferguson**

I built this to solve a real problem I face as a business analyst. It's a portfolio project demonstrating my skills in AI integration, prompt engineering, and full-stack development with Flask.

---

**Ready to use?** Follow the Quick Start guide above and start chatting!
