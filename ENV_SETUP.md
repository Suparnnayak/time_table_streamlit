# Environment Variables Setup Guide

## Local Development

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Create .env File
Copy the example file:
```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

### Step 3: Edit .env File
Open `.env` and fill in your values:

```env
API_KEY=sk-edu-chatbot-abc123xyz789
GEMINI_API_KEY=your-actual-gemini-api-key
```

### Step 4: Run the Server
```bash
python app.py
```

The app will automatically load variables from `.env` file.

---

## Production Deployment (Render)

### Option 1: Using Render Dashboard (Recommended)

1. Go to your Render service dashboard
2. Navigate to **Environment** tab
3. Add environment variables:

   **API_KEY**
   - Key: `API_KEY`
   - Value: Your secret API key (e.g., `sk-edu-chatbot-abc123xyz789`)

   **GEMINI_API_KEY**
   - Key: `GEMINI_API_KEY`
   - Value: Your Google Gemini API key

4. Click **Save Changes**
5. Redeploy your service

### Option 2: Using render.yaml

The `render.yaml` file already includes environment variable configuration:

```yaml
envVars:
  - key: GEMINI_API_KEY
    sync: false
  - key: API_KEY
    sync: false
    generateValue: true
```

When deploying via Blueprint, Render will prompt you to set these values.

---

## Environment Variables Reference

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `API_KEY` | Secret key for API authentication | `sk-edu-chatbot-abc123xyz789` |
| `GEMINI_API_KEY` | Google Gemini API key | `AIzaSy...` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `8080` (local), `10000` (Render) |
| `FLASK_ENV` | Flask environment | `production` |

---

## Security Notes

1. **Never commit `.env` file** - It's already in `.gitignore`
2. **Never share API keys** - Keep them secret
3. **Use different keys** - Use different `API_KEY` for development and production
4. **Rotate keys** - Change keys if compromised

---

## Troubleshooting

### "API key is missing" Error

**Local Development:**
- Check that `.env` file exists
- Verify `.env` file has `API_KEY=` line
- Make sure there are no spaces: `API_KEY=value` (not `API_KEY = value`)

**Production (Render):**
- Go to Render dashboard → Environment tab
- Verify `API_KEY` is set
- Check that value doesn't have extra spaces
- Redeploy after setting variables

### "Gemini API key not configured" Error

**Local Development:**
- Check `.env` file has `GEMINI_API_KEY=` line
- Verify the key is correct

**Production (Render):**
- Set `GEMINI_API_KEY` in Render environment variables
- Redeploy service

### Variables Not Loading

1. Make sure `python-dotenv` is installed:
   ```bash
   pip install python-dotenv
   ```

2. Verify `.env` file is in the same directory as `app.py`

3. Check file format (no spaces around `=`):
   ```env
   # ✅ Correct
   API_KEY=value
   
   # ❌ Wrong
   API_KEY = value
   ```

---

## Testing Environment Variables

### Check if variables are loaded:

```python
# In Python shell
from dotenv import load_dotenv
import os

load_dotenv()
print("API_KEY:", "✅ Set" if os.getenv('API_KEY') else "❌ Not set")
print("GEMINI_API_KEY:", "✅ Set" if os.getenv('GEMINI_API_KEY') else "❌ Not set")
```

### Test API health endpoint:

```bash
curl http://localhost:8080/api/health
```

Should show:
```json
{
  "api_key_configured": true,
  "gemini_configured": true
}
```

---

## Quick Start Checklist

- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Copy `.env.example` to `.env`
- [ ] Fill in `API_KEY` in `.env`
- [ ] Fill in `GEMINI_API_KEY` in `.env`
- [ ] Test locally: `python app.py`
- [ ] Set variables in Render dashboard (for production)
- [ ] Deploy to Render

---

**Your environment is now properly configured! 🎉**

