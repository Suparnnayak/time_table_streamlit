# Deploy to Render & Connect with React - Simple Guide

## Part 1: Deploy to Render

### Step 1: Push Code to GitHub
```bash
git init
git add .
git commit -m "Educational Chatbot API"
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

### Step 2: Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up (free tier available)
3. Connect your GitHub account

### Step 3: Create New Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Select your repository

### Step 4: Configure Service
- **Name:** `educational-chatbot-api` (or any name)
- **Environment:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

### Step 5: Set Environment Variables
Click **"Advanced"** → **"Add Environment Variable"**

Add these 2 variables:

**Variable 1:**
- Key: `API_KEY`
- Value: `sk-edu-chatbot-abc123xyz789` (generate a random secret string)

**Variable 2:**
- Key: `GEMINI_API_KEY`
- Value: Your Google Gemini API key (from https://makersuite.google.com/app/apikey)

### Step 6: Deploy
1. Click **"Create Web Service"**
2. Wait 2-5 minutes for deployment
3. Your API will be live at: `https://your-app-name.onrender.com`

---

## Part 2: Connect React Frontend

### Step 1: Get Your API Details

After deployment, you'll have:
- **API URL:** `https://your-app-name.onrender.com`
- **API Key:** The value you set for `API_KEY` in Render (e.g., `sk-edu-chatbot-abc123xyz789`)

### Step 2: Create React Environment File

In your React project root, create `.env` file:

```env
REACT_APP_API_URL=https://your-app-name.onrender.com
REACT_APP_API_KEY=sk-edu-chatbot-abc123xyz789
```

**Important:** 
- React requires `REACT_APP_` prefix for environment variables
- Never commit `.env` to Git (add to `.gitignore`)

### Step 3: Create API Service (React)

Create `src/services/api.js`:

```javascript
const API_URL = process.env.REACT_APP_API_URL;
const API_KEY = process.env.REACT_APP_API_KEY;

export const sendMessage = async (message) => {
  try {
    const response = await fetch(`${API_URL}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': API_KEY
      },
      body: JSON.stringify({ message })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Failed to get response');
    }

    const data = await response.json();
    return data.response;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export const checkHealth = async () => {
  try {
    const response = await fetch(`${API_URL}/api/health`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Health check failed:', error);
    throw error;
  }
};
```

### Step 4: Use in React Component

Example component `src/components/Chatbot.js`:

```javascript
import React, { useState } from 'react';
import { sendMessage } from '../services/api';

function Chatbot() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!message.trim()) return;

    setLoading(true);
    try {
      const aiResponse = await sendMessage(message);
      setResponse(aiResponse);
      setMessage('');
    } catch (error) {
      setResponse(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chatbot">
      <h2>Educational Chatbot</h2>
      
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask about education, courses, skills..."
          disabled={loading}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Sending...' : 'Send'}
        </button>
      </form>

      {response && (
        <div className="response">
          <h3>Response:</h3>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default Chatbot;
```

### Step 5: Add to .gitignore

Make sure your React `.gitignore` includes:
```
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
```

---

## Quick Test

### Test API from Browser
1. Open: `https://your-app-name.onrender.com/api/health`
2. Should see: `{"status": "healthy", ...}`

### Test from React
```javascript
// In your React component
useEffect(() => {
  checkHealth().then(data => {
    console.log('API is healthy:', data);
  });
}, []);
```

---

## Troubleshooting

### CORS Error
- Already handled! CORS is enabled in the Flask app
- If you still get errors, check the API URL is correct

### 401 Unauthorized
- Check `REACT_APP_API_KEY` matches the `API_KEY` in Render
- Verify the API key is in the request header

### API Not Responding
- Check Render dashboard for service status
- First request after 15 min inactivity takes ~30 seconds (free tier spin-down)
- Check Render logs for errors

---

## Summary

1. ✅ Deploy to Render (set `API_KEY` and `GEMINI_API_KEY`)
2. ✅ Get your API URL and API Key
3. ✅ Add to React `.env` file
4. ✅ Create API service in React
5. ✅ Use in components

**Your React app is now connected to your deployed API! 🚀**

