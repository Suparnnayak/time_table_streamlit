# Quick Start - API Only Setup

## ✅ What's Changed

1. ✅ **Removed HTML** - Pure API now, no frontend
2. ✅ **Added API Key Authentication** - Secure your API
3. ✅ **API Documentation** - Visit `/` for full docs
4. ✅ **Render Ready** - All deployment files included

---

## 🔑 API Key Setup

### For You (Server Side)
Set in Render environment variables:
- `API_KEY` - The secret key you'll share with your team
- `GEMINI_API_KEY` - Your Google Gemini API key

### For Your Team (Frontend)
They need:
- **API URL:** `https://your-app-name.onrender.com`
- **API Key:** The value you set for `API_KEY`

---

## 📡 API Endpoints

### Public (No Auth)
- `GET /` - API documentation
- `GET /api/health` - Health check

### Protected (Requires API Key)
- `POST /api/chat` - Chat with the bot
- `GET /api/models` - List available models

---

## 🚀 Deploy to Render

1. Push code to GitHub
2. Connect to Render
3. Set environment variables:
   - `GEMINI_API_KEY` = Your Gemini key
   - `API_KEY` = Secret key for your team
4. Deploy!

See `DEPLOY_RENDER.md` for detailed steps.

---

## 📝 Give to Your Team

Share these files:
- `API_DOCUMENTATION.md` - Complete API docs
- The API URL and API key

They can integrate using:
- JavaScript/Fetch
- React
- Vue
- Any frontend framework

---

## 🧪 Test Locally

```bash
# Set API key
export API_KEY=test-key-123
export GEMINI_API_KEY=your-gemini-key

# Run server
python app.py

# Test (in another terminal)
curl -X POST http://localhost:8080/api/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: test-key-123" \
  -d '{"message": "What is Python?"}'
```

---

**Your API is ready for deployment! 🎉**

