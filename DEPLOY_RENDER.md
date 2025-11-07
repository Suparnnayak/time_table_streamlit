# Deploying to Render - Step by Step Guide

## Prerequisites
- GitHub account
- Render account (free tier available)
- Your code pushed to GitHub

---

## Step 1: Push Code to GitHub

1. Initialize git (if not already done):
```bash
git init
git add .
git commit -m "Initial commit - Educational Chatbot API"
```

2. Create a new repository on GitHub

3. Push your code:
```bash
git remote add origin https://github.com/yourusername/your-repo-name.git
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy on Render

### Option A: Using render.yaml (Recommended)

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repository
4. Render will automatically detect `render.yaml` and deploy
5. Set environment variables (see Step 3)

### Option B: Manual Setup

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name:** `educational-chatbot-api`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **"Create Web Service"**

---

## Step 3: Set Environment Variables

In Render dashboard, go to your service → **Environment** tab:

Add these environment variables:

1. **GEMINI_API_KEY**
   - Value: Your Google Gemini API key
   - Get it from: https://makersuite.google.com/app/apikey

2. **API_KEY**
   - Value: A secret key for your API (e.g., generate a random string)
   - This is what you'll give to your frontend team
   - Example: `sk-edu-chatbot-abc123xyz789`
   - **Important:** Keep this secret and share only with your team

3. **PORT** (Optional)
   - Render sets this automatically, but you can set it to `10000` if needed

---

## Step 4: Deploy

1. Click **"Manual Deploy"** → **"Deploy latest commit"**
2. Wait for deployment to complete (usually 2-5 minutes)
3. Your API will be available at: `https://your-app-name.onrender.com`

---

## Step 5: Test Your API

### Test Health Endpoint
```bash
curl https://your-app-name.onrender.com/api/health
```

### Test Chat Endpoint
```bash
curl -X POST https://your-app-name.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key-here" \
  -d '{"message": "What is Python?"}'
```

### View API Documentation
Open in browser:
```
https://your-app-name.onrender.com/
```

---

## Step 6: Share API Key with Your Team

1. Go to Render Dashboard → Your Service → **Environment**
2. Copy the `API_KEY` value
3. Share this with your frontend team
4. They can use it in their frontend code

**Example for your team:**
```javascript
const API_KEY = 'sk-edu-chatbot-abc123xyz789';
const API_URL = 'https://your-app-name.onrender.com';

fetch(`${API_URL}/api/chat`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': API_KEY
  },
  body: JSON.stringify({
    message: 'User question here'
  })
})
```

---

## Troubleshooting

### Deployment Fails
- Check build logs in Render dashboard
- Ensure `requirements.txt` is correct
- Verify Python version in `runtime.txt`

### API Returns 401 Unauthorized
- Check that `API_KEY` environment variable is set
- Verify the API key in request headers matches

### API Returns 500 Error
- Check Render logs
- Verify `GEMINI_API_KEY` is set correctly
- Check that Gemini API key is valid

### Slow First Request
- Render free tier spins down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds
- Consider upgrading to paid tier for always-on service

---

## Render Free Tier Limitations

- ✅ 750 hours/month free
- ✅ Automatic HTTPS
- ✅ Auto-deploy from GitHub
- ⚠️ Spins down after 15 min inactivity (cold start ~30s)
- ⚠️ Limited to 512MB RAM

---

## Updating Your API

1. Make changes to your code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update API"
   git push
   ```
3. Render automatically deploys (or manually trigger in dashboard)

---

## Custom Domain (Optional)

1. Go to Render Dashboard → Your Service → **Settings**
2. Scroll to **"Custom Domains"**
3. Add your domain
4. Follow DNS configuration instructions

---

**Your API is now live! 🚀**

Share the API URL and API key with your frontend team.

