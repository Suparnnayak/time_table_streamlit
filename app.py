from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for website integration

# Configure Gemini API (set via environment variable)
# For local development: Set GEMINI_API_KEY environment variable
# For production (Render): Set GEMINI_API_KEY in Render dashboard environment variables
# This is the ONLY key needed - kept secure on server side
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

# Configure Gemini model
# Try different model names (prioritize newer stable models)
MODEL_NAMES = [
    'gemini-2.5-flash',      # Latest stable fast model (recommended - try this first)
    'gemini-2.5-pro',        # Latest stable powerful model
    'gemini-2.0-flash',      # Stable fast model
    'gemini-2.0-flash-001',  # Stable version
    'gemini-1.5-flash',      # Older but still works
    'gemini-1.5-pro',        # Older but still works
    'gemini-flash-latest',   # Latest flash (auto-updates)
    'gemini-pro-latest',     # Latest pro (auto-updates)
]

model = None
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    # Try to initialize with available model
    for model_name in MODEL_NAMES:
        try:
            model = genai.GenerativeModel(model_name)
            print(f"✅ Initialized model: {model_name}")
            break
        except Exception as e:
            error_msg = str(e)
            if '404' in error_msg or 'not found' in error_msg.lower():
                print(f"⚠️  Model {model_name} not found, trying next...")
                continue
            else:
                # Other errors might be okay, try using it
                model = genai.GenerativeModel(model_name)
                print(f"✅ Using model: {model_name}")
                break
    
    # If no model worked, try to list available models and use the best one
    if model is None:
        try:
            print("\n⚠️  Could not auto-detect model. Listing available models...")
            available_models = genai.list_models()
            print("Available models with generateContent support:")
            
            # Prioritize stable models over previews
            stable_models = []
            preview_models = []
            
            for m in available_models:
                if 'generateContent' in m.supported_generation_methods:
                    model_name_clean = m.name.replace('models/', '')
                    if 'preview' in model_name_clean.lower() or 'exp' in model_name_clean.lower():
                        preview_models.append(model_name_clean)
                    else:
                        stable_models.append(model_name_clean)
            
            # Try stable models first
            for model_name_clean in stable_models:
                print(f"  - {model_name_clean} (stable)")
                try:
                    model = genai.GenerativeModel(model_name_clean)
                    print(f"✅ Successfully using stable model: {model_name_clean}\n")
                    break
                except:
                    continue
            
            # If no stable model worked, try preview models
            if model is None:
                for model_name_clean in preview_models[:5]:  # Try first 5 preview models
                    print(f"  - {model_name_clean} (preview)")
                    try:
                        model = genai.GenerativeModel(model_name_clean)
                        print(f"✅ Successfully using preview model: {model_name_clean}\n")
                        break
                    except:
                        continue
                        
        except Exception as e:
            print(f"❌ Error listing models: {str(e)}")
            model = None
            print("\n💡 Tip: Visit http://localhost:8080/api/models to see available models")

# System prompt for educational chatbot
SYSTEM_PROMPT = """You are an expert educational assistant designed EXCLUSIVELY to help users with learning and education-related topics. 

**IMPORTANT: You MUST ONLY answer questions related to education, learning, courses, skills, study methods, academic subjects, career guidance, and educational resources. You MUST politely decline and redirect any non-educational questions (such as cooking recipes, general how-to guides, entertainment, personal advice unrelated to learning, etc.).**

Your capabilities include:

1. **Answering Educational Questions**: Provide clear, accurate, and comprehensive answers to questions about academic subjects, concepts, theories, and educational topics.

2. **Course Suggestions**: Recommend relevant courses, learning paths, and educational programs based on the user's interests, goals, current skill level, and career aspirations. Consider various formats (online, in-person, self-paced, etc.).

3. **Skill Recommendations**: Suggest skills to develop based on:
   - User's current field or interests
   - Industry trends and demands
   - Career goals
   - Complementary skills that enhance existing knowledge

4. **Study Tips and Learning Strategies**: Provide effective study methods, learning techniques, and productivity tips tailored to different learning styles.

5. **Resource Recommendations**: Suggest educational books, websites, platforms, tools, and other learning resources.

6. **Career Guidance**: Offer advice on educational paths that lead to specific careers, including required qualifications, certifications, and experience.

7. **Subject-Specific Help**: Provide detailed explanations, examples, and practice suggestions for any academic subject (mathematics, science, history, literature, programming, etc.).

**Response Guidelines:**
- If a question is NOT related to education, learning, courses, skills, or academic topics, politely decline and redirect:
  Example: "I'm an educational assistant focused on learning and education. I can help you with questions about courses, skills, study methods, or academic subjects. Could you rephrase your question in an educational context, or ask me something about learning instead?"

- Always be encouraging and supportive
- Be clear and concise
- Provide practical and actionable advice
- Stay up-to-date with current educational trends
- Be respectful of different learning styles and backgrounds

When suggesting courses or skills, provide:
- Why it's valuable
- Where to learn it (platforms, institutions)
- Prerequisites if any
- Estimated time commitment
- Career applications

Format your responses in a friendly, conversational manner while maintaining professionalism. Use bullet points, numbered lists, and clear sections to make information easy to digest."""

# No API key authentication needed - API is publicly accessible
# Only GEMINI_API_KEY is required (server-side only, never exposed to clients)

@app.route('/', methods=['GET'])
def api_docs():
    """API Documentation endpoint"""
    base_url = request.host_url.rstrip('/')
    return jsonify({
        'name': 'Educational Chatbot API',
        'version': '1.0.0',
        'description': 'RESTful API for educational chatbot powered by Google Gemini',
        'base_url': base_url,
        'authentication': {
            'type': 'None - Public API',
            'note': 'No authentication required. Just use the API URL directly.'
        },
        'endpoints': {
            'GET /': {
                'description': 'API documentation (this endpoint)',
                'authentication': False
            },
            'GET /api/health': {
                'description': 'Health check endpoint',
                'authentication': False,
                'response': {
                    'status': 'healthy',
                    'gemini_configured': 'boolean',
                    'model_initialized': 'boolean'
                }
            },
            'POST /api/chat': {
                'description': 'Send a message to the educational chatbot',
                'authentication': False,
                'request_body': {
                    'message': 'string (required) - Your educational question or query'
                },
                'response': {
                    'response': 'string - AI generated response',
                    'timestamp': 'string - ISO format timestamp'
                },
                'example_request': {
                    'message': 'What courses should I take for web development?'
                },
                'example_response': {
                    'response': 'For web development, I recommend...',
                    'timestamp': '2024-01-01T12:00:00'
                }
            },
            'GET /api/models': {
                'description': 'List available Gemini models',
                'authentication': False,
                'response': {
                    'available_models': 'array - List of available models',
                    'current_model': 'string - Currently active model'
                }
            }
        },
        'usage_examples': {
            'curl': f'''
# Health check (no auth required)
curl {base_url}/api/health

# Chat request (no authentication needed)
curl -X POST {base_url}/api/chat \\
  -H "Content-Type: application/json" \\
  -d '{{"message": "What is Python programming?"}}'
''',
            'javascript': f'''
// Using fetch API (no authentication needed)
fetch('{base_url}/api/chat', {{
  method: 'POST',
  headers: {{
    'Content-Type': 'application/json'
  }},
  body: JSON.stringify({{
    message: 'What courses should I take for data science?'
  }})
}})
.then(response => response.json())
.then(data => console.log(data.response))
.catch(error => console.error('Error:', error));
''',
            'python': f'''
import requests

response = requests.post(
    '{base_url}/api/chat',
    headers={{
        'Content-Type': 'application/json'
    }},
    json={{
        'message': 'What skills do I need for machine learning?'
    }}
)

data = response.json()
print(data['response'])
'''
        },
        'error_responses': {
            '400': 'Bad Request - Missing or invalid request body',
            '500': 'Internal Server Error - Check server logs for details'
        }
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        if not GEMINI_API_KEY:
            return jsonify({
                'error': 'Gemini API key is not configured. Please set GEMINI_API_KEY environment variable.'
            }), 500
        
        if not model:
            return jsonify({
                'error': 'Gemini model is not initialized. Please check your API key and model availability.'
            }), 500
        
        # Create conversation with system prompt
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nAssistant:"
        
        # Generate response using Gemini
        try:
            response = model.generate_content(full_prompt)
            
            # Extract the text response
            if hasattr(response, 'text') and response.text:
                assistant_response = response.text
            elif hasattr(response, 'candidates') and response.candidates:
                # Fallback for different response formats
                assistant_response = response.candidates[0].content.parts[0].text
            else:
                assistant_response = "Sorry, I couldn't generate a response. Please try again."
            
            return jsonify({
                'response': assistant_response,
                'timestamp': datetime.now().isoformat()
            })
        except Exception as gen_error:
            error_msg = str(gen_error)
            print(f"Gemini API Error: {error_msg}")
            
            # Provide helpful error messages
            if '404' in error_msg or 'not found' in error_msg.lower():
                return jsonify({
                    'error': f'Model not found. Error: {error_msg}. Please check if the model name is correct.'
                }), 500
            elif '403' in error_msg or 'permission' in error_msg.lower():
                return jsonify({
                    'error': 'API key permission denied. Please check your API key permissions.'
                }), 500
            elif '429' in error_msg or 'quota' in error_msg.lower():
                return jsonify({
                    'error': 'API quota exceeded. Please check your API usage limits.'
                }), 429
            else:
                return jsonify({
                    'error': f'Gemini API error: {error_msg}'
                }), 500
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'gemini_configured': bool(GEMINI_API_KEY),
        'model_initialized': model is not None,
        'message': 'API is running. Set GEMINI_API_KEY environment variable for full functionality.',
        'authentication': 'None - Public API'
    })

@app.route('/api/models', methods=['GET'])
def list_models():
    """List available Gemini models (for debugging)"""
    try:
        if not GEMINI_API_KEY:
            return jsonify({
                'error': 'API key not configured'
            }), 500
        
        available_models = genai.list_models()
        models_list = []
        for m in available_models:
            if 'generateContent' in m.supported_generation_methods:
                models_list.append({
                    'name': m.name,
                    'display_name': m.display_name,
                    'description': m.description
                })
        
        return jsonify({
            'available_models': models_list,
            'current_model': str(model) if model else None
        })
    except Exception as e:
        return jsonify({
            'error': f'Failed to list models: {str(e)}'
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))  
    debug = os.getenv('FLASK_ENV') == 'development'
    
    print("\n" + "="*60)
    print("🎓 Educational Chatbot - Flask Server Starting")
    print("="*60)
    print(f"📍 Server running on: http://localhost:{port}")
    print(f"📍 Alternative URL: http://127.0.0.1:{port}")
    print(f"🔧 Debug mode: {'ON' if debug else 'OFF'}")
    print(f"🔑 Gemini API: {'✅ Configured' if GEMINI_API_KEY else '❌ Not configured'}")
    if not GEMINI_API_KEY:
        print("⚠️  WARNING: GEMINI_API_KEY not set. Chat functionality will not work.")
    print("🌐 API is publicly accessible - no authentication required")
    print("="*60)
    print("Press CTRL+C to stop the server")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=port, debug=debug)

