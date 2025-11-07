# Educational Chatbot 🎓

A Python-based educational chatbot using Google Gemini API (free!) that can answer educational questions, suggest courses, recommend skills, and provide learning guidance. The chatbot can be integrated into any website.

## Features

- 🤖 **Intelligent Conversations**: Powered by Google's Gemini Pro (free API)
- 📚 **Course Suggestions**: Get personalized course recommendations
- 🎯 **Skill Recommendations**: Discover skills to develop
- 💡 **Study Tips**: Receive effective learning strategies
- 📖 **Educational Q&A**: Ask questions about any subject
- 🌐 **Website Integration**: Easy to embed in any website
- 🎨 **Modern UI**: Beautiful, responsive interface
- 🆓 **Free to Use**: Uses Google Gemini (free tier available)

## Prerequisites

- Python 3.8 or higher
- A Google Gemini API key ([Get one here for free](https://makersuite.google.com/app/apikey))

## Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd "education chatbot"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Gemini API key**
   
   **Option A: Environment Variable (Recommended)**
   ```bash
   # Windows (PowerShell)
   $env:GEMINI_API_KEY="your_api_key_here"
   
   # Windows (CMD)
   set GEMINI_API_KEY=your_api_key_here
   
   # Linux/Mac
   export GEMINI_API_KEY="your_api_key_here"
   ```
   
   **Option B: Create a `.env` file** (you'll need python-dotenv package)
   ```bash
   pip install python-dotenv
   ```
   Create a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   - Navigate to [http://localhost:5000](http://localhost:5000)
   - You'll see the full-page chatbot interface

3. **Start chatting!**
   - Ask questions about any educational topic
   - Request course suggestions
   - Ask for skill recommendations
   - Get study tips and learning strategies

## Integrating into Your Website

### Method 1: Embed the Widget (Recommended)

1. **Copy the widget code** from `chatbot_widget.html`
2. **Update the API URL** in the script section:
   ```javascript
   const CHATBOT_API_URL = 'https://your-domain.com/api/chat';
   ```
3. **Paste the entire widget code** into your website's HTML (before `</body>` tag)
4. **Deploy your Flask app** to a server (see Deployment section)

### Method 2: Use the API Directly

Make POST requests to `/api/chat`:

```javascript
fetch('http://localhost:5000/api/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        message: 'What courses should I take for web development?'
    })
})
.then(response => response.json())
.then(data => console.log(data.response));
```

### Method 3: Iframe Embedding

You can embed the full chatbot page in an iframe:

```html
<iframe 
    src="http://localhost:5000" 
    width="100%" 
    height="600px" 
    frameborder="0"
></iframe>
```

## API Endpoints

### POST `/api/chat`
Send a message to the chatbot.

**Request:**
```json
{
    "message": "What skills do I need for data science?"
}
```

**Response:**
```json
{
    "response": "For data science, you'll need...",
    "timestamp": "2024-01-01T12:00:00"
}
```

### GET `/api/health`
Check if the API is running and configured.

**Response:**
```json
{
    "status": "healthy",
    "gemini_configured": true
}
```

## Example Questions

- "What courses should I take to become a data scientist?"
- "What skills do I need for web development?"
- "How can I improve my study habits?"
- "Explain quantum physics in simple terms"
- "What are the best resources to learn Python?"
- "Suggest a learning path for machine learning"
- "What certifications are valuable for cybersecurity?"

## Deployment

### Deploy to Heroku

1. Create a `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Install gunicorn:
   ```bash
   pip install gunicorn
   ```

3. Set environment variable in Heroku:
   ```bash
   heroku config:set GEMINI_API_KEY=your_api_key
   ```

4. Deploy:
   ```bash
   git push heroku main
   ```

### Deploy to PythonAnywhere

1. Upload your files to PythonAnywhere
2. Set up a web app pointing to `app.py`
3. Set environment variable in the web app configuration
4. Reload the web app

### Deploy to Railway/Render

1. Connect your repository
2. Set `GEMINI_API_KEY` in environment variables
3. Set start command: `python app.py`
4. Deploy!

## Configuration

### Change the Port

Set the `PORT` environment variable:
```bash
export PORT=8080
python app.py
```

### Customize the System Prompt

Edit the `SYSTEM_PROMPT` variable in `app.py` to change the chatbot's behavior and personality.

### Enable Debug Mode

```bash
export FLASK_ENV=development
python app.py
```

## Troubleshooting

### API Key Issues
- Ensure your `GEMINI_API_KEY` is set correctly
- Check that the API key is valid and has not expired
- Verify you're using the correct environment variable name

### CORS Issues
- The app includes `flask-cors` for cross-origin requests
- If you still have issues, check your server's CORS settings

### Connection Errors
- Make sure the Flask server is running
- Check that the port is not blocked by a firewall
- Verify the API URL in your frontend code matches your server URL

## Project Structure

```
education-chatbot/
├── app.py                 # Flask application and API
├── requirements.txt       # Python dependencies
├── chatbot_widget.html    # Embeddable widget code
└── README.md             # This file
```

## Technologies Used

- **Flask**: Web framework for Python
- **Google Gemini API**: Free AI model for chat
- **Flask-CORS**: Enable cross-origin requests
- **HTML/CSS/JavaScript**: Frontend interface

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

---

**Happy Learning! 🚀**

