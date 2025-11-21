# 🤖 Business Intelligence Assistant

> **An AI-powered chatbot that helps you create reports, understand metrics, and get business intelligence guidance - completely FREE!**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)

---

## 📖 What Is This?

A **Business Intelligence Assistant** that acts as your AI consultant for:
- 📊 Creating report outlines and structures
- 📈 Explaining business metrics and KPIs
- 🔍 Providing data analysis guidance
- 📝 Generating presentation frameworks
- 💡 Answering business intelligence questions

**No API keys needed!** Uses Ollama (free, local AI) - works completely offline.

---

## 🎯 The Problem It Solves

**Daily Challenge:** Business analysts spend 4-6 hours creating reports, explaining metrics, and structuring presentations. This involves:
- Switching between multiple tools (Excel, Power BI, PowerPoint)
- Constantly Googling metric definitions
- Figuring out report structures
- Explaining complex concepts to stakeholders

**Solution:** This chatbot provides instant guidance, saving **70-80% of your time** while improving quality and consistency.

---

## ✨ Features

- ✅ **100% FREE** - No API keys, no credits needed
- ✅ **Works Offline** - Uses local AI (Ollama)
- ✅ **Natural Language** - Ask questions in plain English
- ✅ **Professional Output** - Formatted responses ready for business use
- ✅ **Multiple Use Cases** - Reports, metrics, analysis, presentations
- ✅ **Clean Interface** - Modern, easy-to-use web UI

---

## 🚀 Quick Start (5 Minutes)

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

**That's it!** You should see the chat interface. Start asking questions! 🎉

---

## 💬 How to Use

### Basic Usage

1. **Type your question** in the input box at the bottom
2. **Press Enter** or click "Send"
3. **Wait for response** (usually 10-30 seconds)
4. **Read the answer** - it's formatted and ready to use!

### Example Questions

#### 📊 Report Generation
```
"Create a quarterly sales report outline"
"Help me create a presentation about Q4 performance"
"Generate a customer analysis report structure"
```

#### 📈 Metric Explanations
```
"What is customer churn rate and how do I calculate it?"
"Explain revenue vs profit in simple terms"
"What does ROI mean in business?"
```

#### 🔍 Analysis Guidance
```
"I have sales data for 2024, what should I analyze?"
"What metrics should I track for customer retention?"
"Help me plan an analysis of our marketing campaigns"
```

#### 📝 Presentation Help
```
"Help me create a presentation about our Q4 performance for the board meeting"
"I need to explain why sales increased 15%, create a presentation structure"
```

---

## 🖥️ Accessing the Application

Once the application is running, access it at:

### **http://localhost:5000**

**What is localhost?**
- `localhost` = your own computer
- `5000` = the port number where the app runs
- Just type this address in any web browser (Chrome, Firefox, Edge, etc.)

**Important:** The application must be running (Step 5) for the website to work!

---

## 📁 Project Structure

```
bi-assistant/
├── app_ollama.py          # Main application (USE THIS ONE!)
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

---

## 🐛 Troubleshooting

### "python is not recognized"
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

### "File not found" or "can't open file"
- You're not in the correct folder
- Navigate to the project folder (Step 4)
- Make sure you see `app_ollama.py` when you type `dir` or `ls`

### Application starts but responses are slow
- First response is always slower (model loading)
- Subsequent responses are faster
- Make sure your computer has enough RAM (4GB+ recommended)

---

## 📋 Quick Reference

### Starting the App:
```bash
cd bi-assistant
python app_ollama.py
```
Then open: http://localhost:5000

### Common Questions:
- "Create a [type] report outline"
- "What is [metric] and how do I calculate it?"
- "I have [data], what should I analyze?"
- "Help me create a presentation about [topic]"

### Stop the Application:
- Press `Ctrl + C` in the terminal window

---

## 🎯 Summary

**To run the website:**
1. ✅ Python installed
2. ✅ Ollama installed
3. ✅ Model downloaded (`ollama pull llama3`)
4. ✅ Dependencies installed (`pip install -r requirements.txt`)
5. ✅ Application running (`python app_ollama.py`)
6. ✅ Browser open at `http://localhost:5000`

**That's it!** You're ready to use the Business Intelligence Assistant! 🚀

---

## 📄 License

This project is open source and available for portfolio use.

---

## 👤 Author

**Vivian Ferguson**
- Portfolio project demonstrating AI integration and prompt engineering
- Created for academic/portfolio purposes

---

## 🙏 Acknowledgments

- **Ollama** - For providing free, local LLM capabilities
- **Flask** - Excellent Python web framework
- **Business Intelligence Community** - For inspiration and use cases

---

**Ready to use?** Follow the Quick Start guide above and start chatting! 🚀

