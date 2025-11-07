# Simple Deployment & React Connection

## 🚀 Deploy to Render (5 Steps)

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Educational Chatbot API"
git push
```

### Step 2: Go to Render
1. Visit [render.com](https://render.com)
2. Sign up / Login
3. Click **"New +"** → **"Web Service"**

### Step 3: Connect Repository
- Select your GitHub repository
- Click **"Connect"**

### Step 4: Configure
- **Name:** `educational-chatbot-api`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

### Step 5: Set Environment Variable
Click **"Advanced"** → **"Add Environment Variable"**

**Only ONE variable needed:**
- **Key:** `GEMINI_API_KEY`
- **Value:** Your Gemini API key (from https://makersuite.google.com/app/apikey)

Click **"Create Web Service"** and wait 2-5 minutes.

**Done!** Your API is live at: `https://your-app-name.onrender.com`

---

## 🔗 Connect React (Super Simple)

### Step 1: Get Your API URL
After deployment, copy your Render URL:
```
https://your-app-name.onrender.com
```

### Step 2: Use in React (No API Key Needed!)

**Simple Example:**
```javascript
// In your React component
const sendMessage = async (message) => {
  const response = await fetch('https://your-app-name.onrender.com/api/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message })
  });
  
  const data = await response.json();
  return data.response;
};

// Use it
const response = await sendMessage("What is Python?");
console.log(response);
```

**Complete React Component:**
```javascript
import React, { useState } from 'react';

function Chatbot() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const API_URL = 'https://your-app-name.onrender.com';

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const res = await fetch(`${API_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
      });
      
      const data = await res.json();
      setResponse(data.response);
      setMessage('');
    } catch (error) {
      setResponse('Error: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask about education..."
        />
        <button disabled={loading}>
          {loading ? 'Sending...' : 'Send'}
        </button>
      </form>
      {response && <div>{response}</div>}
    </div>
  );
}

export default Chatbot;
```

---

## ✅ That's It!

1. ✅ Deploy to Render (set only `GEMINI_API_KEY`)
2. ✅ Share the URL with your team
3. ✅ They use it directly in React (no API key needed!)

**No authentication, no API keys to share - just the URL!** 🎉

