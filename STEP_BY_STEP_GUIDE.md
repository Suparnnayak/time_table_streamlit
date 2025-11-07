# Step-by-Step Guide: Running Your Flask Educational Chatbot 🚀

## Prerequisites Check

### Step 1: Verify Python Installation
Open PowerShell or Command Prompt and run:
```bash
python --version
```
**Expected Output:** Python 3.8 or higher (e.g., `Python 3.12.7`)

If Python is not installed, download from [python.org](https://www.python.org/downloads/)

---

## Installation Steps

### Step 2: Navigate to Project Folder
```bash
cd "d:\education chatbot"
```

### Step 3: Install Required Packages
```bash
pip install -r requirements.txt
```

**What this installs:**
- Flask (web framework)
- flask-cors (for cross-origin requests)
- google-generativeai (Gemini API)

**Expected Output:**
```
Successfully installed Flask-3.0.0 flask-cors-4.0.0 google-generativeai-0.3.2 ...
```

---

## Running the Flask Application

### Step 4: Start the Flask Server

**Option A: Direct Python Command**
```bash
python app.py
```

**Option B: Using Flask Command (Alternative)**
```bash
flask run
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Step 5: Verify Server is Running

You should see:
- ✅ No error messages
- ✅ "Running on http://127.0.0.1:5000" message
- ✅ Server stays running (doesn't exit)

---

## Testing the Flask API

### Step 6: Test the Health Endpoint

**Option A: Using Browser**
Open your browser and go to:
```
http://localhost:5000/api/health
```

**Expected Response (JSON):**
```json
{
  "status": "healthy",
  "gemini_configured": true
}
```

**Option B: Using PowerShell (curl)**
```powershell
curl http://localhost:5000/api/health
```

**Option C: Using Python Test Script**
Run the test script:
```bash
python test_api.py
```

### Step 7: Test the Chat API

**Using PowerShell:**
```powershell
$body = @{
    message = "What is Python?"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/api/chat" -Method POST -Body $body -ContentType "application/json"
```

**Using Python:**
```python
import requests

response = requests.post('http://localhost:5000/api/chat', 
    json={'message': 'What is Python?'})
print(response.json())
```

---

## Using the Web Interface

### Step 8: Open the Chatbot in Browser

1. Make sure Flask server is running (Step 4)
2. Open your web browser
3. Navigate to: **http://localhost:5000**
4. You should see the chatbot interface

### Step 9: Test the Chatbot

1. Type a message in the input box (e.g., "What courses should I take for web development?")
2. Click "Send" or press Enter
3. Wait for the AI response
4. Verify the response appears in the chat

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install flask flask-cors google-generativeai
```

### Problem: "Address already in use"
**Solution:** Port 5000 is already in use. Either:
- Close the other application using port 5000
- Change port in `app.py` (line 419): `port = int(os.getenv('PORT', 8080))`

### Problem: "API key not configured"
**Solution:** The API key is already set in `app.py` line 14. If you see this error, check:
- The API key is correct
- You have internet connection
- Gemini API is accessible

### Problem: Server starts but browser shows "This site can't be reached"
**Solution:**
- Make sure you're using `http://localhost:5000` (not https)
- Check if firewall is blocking port 5000
- Try `http://127.0.0.1:5000` instead

### Problem: "CORS error" when embedding in website
**Solution:** CORS is already enabled in the code (line 8). If you still get errors:
- Make sure you're accessing from the correct domain
- Check browser console for specific error messages

---

## API Endpoints Reference

### 1. Health Check
- **URL:** `GET http://localhost:5000/api/health`
- **Response:**
  ```json
  {
    "status": "healthy",
    "gemini_configured": true
  }
  ```

### 2. Chat Endpoint
- **URL:** `POST http://localhost:5000/api/chat`
- **Request Body:**
  ```json
  {
    "message": "Your question here"
  }
  ```
- **Response:**
  ```json
  {
    "response": "AI response text",
    "timestamp": "2024-01-01T12:00:00"
  }
  ```

### 3. Web Interface
- **URL:** `GET http://localhost:5000/`
- **Response:** HTML page with chatbot interface

---

## Stopping the Server

### Step 10: Stop Flask Server
1. Go to the terminal where Flask is running
2. Press `Ctrl + C`
3. Server will stop

---

## Next Steps: Deploy to Production

Once everything works locally, you can deploy to:
- **Heroku:** `git push heroku main`
- **PythonAnywhere:** Upload files and configure web app
- **Railway/Render:** Connect GitHub repo and deploy

---

## Quick Reference Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
python app.py

# Test health (in another terminal)
curl http://localhost:5000/api/health

# Stop server
Ctrl + C
```

---

**That's it! Your Flask chatbot is now running! 🎉**

