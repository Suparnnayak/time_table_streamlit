# Quick Start Guide 🚀

## How to Run the Educational Chatbot

### Step 1: Install Dependencies

Open your terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

If you get an error, try:
```bash
pip3 install -r requirements.txt
```

### Step 2: Set Your API Key

**Option A: Set Environment Variable (Recommended)**

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="AIzaSyBd0GWKcHH1SuKcef70diWSBEIBKCrqYeE"
```

**Windows (CMD):**
```cmd
set GEMINI_API_KEY=AIzaSyBd0GWKcHH1SuKcef70diWSBEIBKCrqYeE
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY="AIzaSyBd0GWKcHH1SuKcef70diWSBEIBKCrqYeE"
```

**Option B: Set Directly in Code (Quick Test)**

The API key is already set in `app.py` for quick testing. You can skip this step if you just want to test it quickly.

### Step 3: Run the Server

Simply run:

```bash
python app.py
```

Or if that doesn't work:
```bash
python3 app.py
```

Or use the startup script:
- **Windows:** Double-click `run.bat` or run it from command prompt
- **Linux/Mac:** Run `bash run.sh`

### Step 4: Open in Browser

Once the server starts, you'll see:
```
 * Running on http://0.0.0.0:5000
```

Open your web browser and go to:
```
http://localhost:5000
```

Or:
```
http://127.0.0.1:5000
```

### Step 5: Start Chatting! 💬

The chatbot interface will load. You can now:
- Ask educational questions
- Request course suggestions
- Get skill recommendations
- Ask for study tips

## Troubleshooting

### "Module not found" error
Make sure you installed dependencies:
```bash
pip install -r requirements.txt
```

### "Port already in use" error
Change the port in `app.py` or stop the other application using port 5000.

### "API key not configured" error
Make sure you set the `GEMINI_API_KEY` environment variable or it's set in the code.

### Server won't start
- Make sure Python 3.8+ is installed: `python --version`
- Check that Flask is installed: `pip list | findstr Flask`

## Stopping the Server

Press `Ctrl + C` in the terminal to stop the server.

---

**That's it! Happy learning! 🎓**

