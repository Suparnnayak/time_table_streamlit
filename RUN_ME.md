# 🚀 HOW TO RUN YOUR FLASK CHATBOT - SIMPLE GUIDE

## ⚡ QUICK START (Copy & Paste These Commands)

### Step 1: Open PowerShell or Command Prompt
Press `Win + X` and select "Windows PowerShell" or "Terminal"

### Step 2: Navigate to Your Project
```powershell
cd "d:\education chatbot"
```

### Step 3: Install Dependencies (First Time Only)
```powershell
pip install -r requirements.txt
```

### Step 4: Run Flask Server
```powershell
python app.py
```

### Step 5: Open Browser
Go to: **http://localhost:5000**

---

## 📋 WHAT YOU'LL SEE

When you run `python app.py`, you should see:

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

**✅ If you see this, Flask is running correctly!**

---

## 🧪 TESTING THE API

### Test 1: Health Check (In Browser)
1. Open browser
2. Go to: `http://localhost:5000/api/health`
3. Should see: `{"status": "healthy", "gemini_configured": true}`

### Test 2: Run Test Script (In New Terminal)
Open a **NEW** PowerShell window:
```powershell
cd "d:\education chatbot"
python test_api.py
```

### Test 3: Use the Web Interface
1. Go to: `http://localhost:5000`
2. Type a message
3. Click Send
4. Get AI response!

---

## 🛠️ TROUBLESHOOTING

### Problem: Port 5000 Already in Use

**Solution:** Close the other application or change port

**Option A: Find and Close Process**
```powershell
# Find what's using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with number from above)
taskkill /PID <PID> /F
```

**Option B: Use Different Port**
Edit `app.py` line 419, change:
```python
port = int(os.getenv('PORT', 8080))  # Changed to 8080
```
Then access: `http://localhost:8080`

### Problem: "Module not found"
```powershell
pip install flask flask-cors google-generativeai
```

### Problem: "Can't reach site"
- Make sure Flask server is running
- Use `http://` not `https://`
- Try `http://127.0.0.1:5000`

---

## 📝 COMPLETE COMMAND SEQUENCE

Copy and paste this entire block:

```powershell
# Navigate to project
cd "d:\education chatbot"

# Install dependencies (first time only)
pip install -r requirements.txt

# Start Flask server
python app.py
```

Then open browser: **http://localhost:5000**

---

## 🎯 VERIFICATION CHECKLIST

- [ ] Python is installed (`python --version`)
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Flask server starts without errors
- [ ] Browser can access `http://localhost:5000`
- [ ] Health endpoint works: `http://localhost:5000/api/health`
- [ ] Chatbot responds to messages

---

## 🛑 STOPPING THE SERVER

1. Go to terminal where Flask is running
2. Press `Ctrl + C`
3. Server stops

---

**That's it! Your Flask chatbot should be running! 🎉**

