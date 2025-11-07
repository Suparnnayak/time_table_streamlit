# Complete Flask Setup Guide 🚀

## Quick Start (3 Commands)

```bash
# 1. Navigate to project folder
cd "d:\education chatbot"

# 2. Install dependencies (if not already done)
pip install -r requirements.txt

# 3. Run Flask server
python app.py
```

Then open: **http://localhost:5000**

---

## Detailed Step-by-Step Instructions

### STEP 1: Open Terminal
- Press `Win + R`
- Type `cmd` or `powershell`
- Press Enter

### STEP 2: Navigate to Project
```bash
cd "d:\education chatbot"
```

### STEP 3: Verify Python
```bash
python --version
```
Should show: `Python 3.8` or higher

### STEP 4: Install Dependencies
```bash
pip install -r requirements.txt
```

**What gets installed:**
- Flask 3.0.0 (Web framework)
- flask-cors 4.0.0 (Cross-origin support)
- google-generativeai 0.3.2 (Gemini AI)

### STEP 5: Start Flask Server
```bash
python app.py
```

**You should see:**
```
============================================================
🎓 Educational Chatbot - Flask Server Starting
============================================================
📍 Server running on: http://localhost:5000
📍 Alternative URL: http://127.0.0.1:5000
🔧 Debug mode: OFF
🔑 Gemini API: ✅ Configured
============================================================
Press CTRL+C to stop the server
============================================================

 * Serving Flask app 'app'
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
```

### STEP 6: Test in Browser
1. Open your web browser
2. Go to: **http://localhost:5000**
3. You should see the chatbot interface

### STEP 7: Test API Endpoints

**Health Check:**
- Browser: http://localhost:5000/api/health
- Should return: `{"status": "healthy", "gemini_configured": true}`

**Chat API Test:**
Run in a new terminal:
```bash
python test_api.py
```

---

## Alternative: Using Flask CLI

### Method 1: Flask Run Command
```bash
# Set Flask app
set FLASK_APP=app.py

# Run Flask
flask run
```

### Method 2: Using run_flask.bat (Windows)
Just double-click `run_flask.bat` file

---

## Verifying Flask is Working

### Test 1: Health Endpoint
Open browser: http://localhost:5000/api/health

**Expected JSON:**
```json
{
  "status": "healthy",
  "gemini_configured": true
}
```

### Test 2: Chat API
Run test script:
```bash
python test_api.py
```

**Expected Output:**
```
✅ Health endpoint is working!
✅ Chat endpoint is working!
🎉 All tests passed!
```

### Test 3: Web Interface
1. Open: http://localhost:5000
2. Type a message
3. Click Send
4. Should receive AI response

---

## Flask API Endpoints

### 1. Web Interface
- **URL:** `GET http://localhost:5000/`
- **Description:** Main chatbot web interface
- **Response:** HTML page

### 2. Health Check
- **URL:** `GET http://localhost:5000/api/health`
- **Description:** Check if server is running
- **Response:**
  ```json
  {
    "status": "healthy",
    "gemini_configured": true
  }
  ```

### 3. Chat API
- **URL:** `POST http://localhost:5000/api/chat`
- **Description:** Send message to chatbot
- **Request:**
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

---

## Common Issues & Solutions

### Issue 1: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install flask flask-cors google-generativeai
```

### Issue 2: "Address already in use"
**Cause:** Port 5000 is already in use

**Solution A:** Close other application
```bash
# Find process using port 5000
netstat -ano | findstr :5000
# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

**Solution B:** Change port
Edit `app.py` line 419:
```python
port = int(os.getenv('PORT', 8080))  # Changed from 5000 to 8080
```

### Issue 3: "Connection refused" or "Can't reach site"
**Solutions:**
- Make sure Flask server is running
- Check you're using `http://` not `https://`
- Try `http://127.0.0.1:5000` instead of `localhost`
- Check firewall settings

### Issue 4: "API key not configured"
**Solution:** API key is already set in `app.py`. If you see this:
- Check internet connection
- Verify API key is correct
- Check Gemini API service status

### Issue 5: CORS Errors
**Solution:** CORS is already enabled. If issues persist:
- Make sure you're accessing from correct domain
- Check browser console for specific errors

---

## Flask Development Tips

### Enable Debug Mode
Set environment variable:
```bash
set FLASK_ENV=development
python app.py
```

Or edit `app.py`:
```python
app.run(host='0.0.0.0', port=port, debug=True)
```

### View Flask Logs
All requests and errors will be shown in the terminal where Flask is running.

### Hot Reload
With debug mode ON, Flask automatically reloads when you change code.

---

## Stopping Flask Server

1. Go to terminal where Flask is running
2. Press `Ctrl + C`
3. Server stops

---

## Production Deployment

### For Production, use:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Or use Waitress (Windows-friendly):
```bash
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

---

## Quick Reference

```bash
# Start server
python app.py

# Test API
python test_api.py

# Check health
curl http://localhost:5000/api/health

# Stop server
Ctrl + C
```

---

**Your Flask chatbot is ready! 🎉**

