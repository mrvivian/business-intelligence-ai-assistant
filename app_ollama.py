"""
Business Intelligence Assistant - Using Ollama (FREE, No API Key Required)
A prompt-based AI application to help users understand data insights and generate reports.
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
import json
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path=env_path)

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)  # Enable CORS for all routes

# Configuration
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama3')  # or 'mistral', 'codellama', etc.

print(f"[INFO] Using Ollama at: {OLLAMA_BASE_URL}")
print(f"[INFO] Model: {OLLAMA_MODEL}")
print("[INFO] No API key required - Ollama is free and local!")

# Load prompt templates
def load_prompt_template(template_name):
    """Load prompt template from prompts directory"""
    try:
        template_path = os.path.join(script_dir, 'prompts', f'{template_name}.txt')
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

def get_system_prompt():
    """Get the main system prompt for the BI Assistant"""
    return """You are a Business Intelligence Assistant, an expert AI consultant specializing in data analysis, business metrics, and report generation.

Your role is to help users:
1. Understand business metrics and KPIs
2. Generate structured report outlines
3. Answer questions about data analysis
4. Provide guidance on data visualization
5. Explain business concepts in simple terms

Guidelines:
- Always provide clear, actionable insights
- Use business terminology appropriately
- Structure responses with clear sections
- Be concise but comprehensive
- Ask clarifying questions when needed
- Format outputs professionally (use markdown for structure)

When generating reports:
- Include executive summary
- Add key metrics section
- Provide analysis and insights
- Include recommendations
- Suggest visualizations where appropriate"""

def get_enhanced_prompt(user_input, context=None):
    """Enhance user input with context and system instructions"""
    system_prompt = get_system_prompt()
    
    # Add context if available
    context_text = ""
    if context:
        context_text = f"\n\nPrevious conversation context:\n{context}\n"
    
    # Determine task type and enhance prompt
    task_type = detect_task_type(user_input)
    
    if task_type == "report_generation":
        enhancement = load_prompt_template("report_generation") or ""
    elif task_type == "metric_explanation":
        enhancement = load_prompt_template("metric_explanation") or ""
    elif task_type == "analysis_guidance":
        enhancement = load_prompt_template("analysis_guidance") or ""
    else:
        enhancement = ""
    
    full_prompt = f"{system_prompt}\n\n{enhancement}\n\nUser request: {user_input}{context_text}"
    
    return full_prompt

def detect_task_type(user_input):
    """Detect what type of task the user is requesting"""
    user_lower = user_input.lower()
    
    report_keywords = ["report", "outline", "summary", "presentation", "document"]
    metric_keywords = ["what is", "explain", "meaning", "calculate", "definition"]
    analysis_keywords = ["analyze", "analysis", "insights", "trends", "what should"]
    
    if any(keyword in user_lower for keyword in report_keywords):
        return "report_generation"
    elif any(keyword in user_lower for keyword in metric_keywords):
        return "metric_explanation"
    elif any(keyword in user_lower for keyword in analysis_keywords):
        return "analysis_guidance"
    else:
        return "general"

def call_ollama_api(prompt):
    """Call Ollama API to get AI response"""
    try:
        url = f"{OLLAMA_BASE_URL}/api/generate"
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 1000
            }
        }
        
        response = requests.post(url, json=payload, timeout=120)  # Increased timeout
        response.raise_for_status()
        
        result = response.json()
        response_text = result.get('response', '')
        
        if not response_text:
            raise Exception("Ollama returned empty response. Try again or check Ollama logs.")
        
        return response_text
        
    except requests.exceptions.ConnectionError:
        raise Exception("Cannot connect to Ollama. Make sure Ollama is running. Install from https://ollama.ai")
    except requests.exceptions.Timeout:
        raise Exception("Ollama request timed out (120s). The model might be loading or the prompt is too long. Try a shorter question.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ollama connection error: {str(e)}")
    except Exception as e:
        raise Exception(f"Ollama API error: {str(e)}")

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        print(f"[DEBUG] Received chat request at {datetime.now()}")
        data = request.json
        user_message = data.get('message', '')
        conversation_history = data.get('history', [])
        
        print(f"[DEBUG] User message: {user_message[:50]}...")
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Build simplified prompt for Ollama (faster, more reliable)
        system_instruction = "You are a Business Intelligence Assistant. Help with data analysis, reports, and business metrics. Be clear and professional."
        
        # Add context if available
        if conversation_history:
            context = "\n".join([f"Previous: {msg['user']}" for msg in conversation_history[-2:]])
            full_prompt = f"{system_instruction}\n\n{context}\n\nUser: {user_message}\n\nAssistant:"
        else:
            full_prompt = f"{system_instruction}\n\nUser: {user_message}\n\nAssistant:"
        
        print(f"[DEBUG] Calling Ollama with prompt length: {len(full_prompt)}")
        print(f"[DEBUG] Prompt preview: {full_prompt[:200]}...")
        
        # Call Ollama API with error handling
        try:
            assistant_message = call_ollama_api(full_prompt)
            
            if not assistant_message or len(assistant_message.strip()) == 0:
                raise Exception("Ollama returned empty response")
            
            print(f"[DEBUG] Received response length: {len(assistant_message)}")
            print(f"[DEBUG] Response preview: {assistant_message[:100]}...")
            
            return jsonify({
                'response': assistant_message,
                'timestamp': datetime.now().isoformat()
            })
        except requests.exceptions.ConnectionError:
            raise Exception("Cannot connect to Ollama. Make sure Ollama is running. Check: ollama list")
        except requests.exceptions.Timeout:
            raise Exception("Ollama request timed out. Try a shorter question or wait a moment and try again.")
        
    except requests.exceptions.ConnectionError as e:
        error_msg = "Cannot connect to Ollama. Make sure Ollama is running."
        print(f"[ERROR] Ollama connection error: {e}")
        return jsonify({'error': error_msg}), 500
    except requests.exceptions.Timeout as e:
        error_msg = "Ollama request timed out. The model might be loading or the prompt is too long."
        print(f"[ERROR] Ollama timeout: {e}")
        return jsonify({'error': error_msg}), 500
    except Exception as e:
        error_msg = str(e)
        print(f"[ERROR] Chat error: {error_msg}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f"Server error: {error_msg}"}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    try:
        # Check if Ollama is running
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        return jsonify({
            'status': 'healthy', 
            'service': 'BI Assistant (Ollama)',
            'ollama_connected': True
        })
    except:
        return jsonify({
            'status': 'degraded',
            'service': 'BI Assistant (Ollama)',
            'ollama_connected': False,
            'message': 'Ollama not running. Install from https://ollama.ai'
        }), 503

if __name__ == '__main__':
    print("=" * 60)
    print("Business Intelligence Assistant - Using Ollama")
    print("=" * 60)
    print(f"Ollama URL: {OLLAMA_BASE_URL}")
    print(f"Model: {OLLAMA_MODEL}")
    print("\nTo use this app:")
    print("1. Install Ollama from https://ollama.ai")
    print(f"2. Run: ollama pull {OLLAMA_MODEL}")
    print("3. Make sure Ollama is running")
    print("=" * 60)
    print("\nStarting Flask application...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)

