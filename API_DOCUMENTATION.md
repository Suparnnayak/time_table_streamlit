# Educational Chatbot API Documentation

## Base URL
```
https://your-app-name.onrender.com
```

## Authentication

All API endpoints (except `/` and `/api/health`) require API key authentication.

### Using X-API-Key Header (Recommended)
```http
X-API-Key: your-api-key-here
```

### Using Authorization Bearer Token
```http
Authorization: Bearer your-api-key-here
```

---

## Endpoints

### 1. API Documentation
**GET** `/`

Returns API documentation and usage examples.

**Authentication:** Not required

**Response:**
```json
{
  "name": "Educational Chatbot API",
  "version": "1.0.0",
  "description": "RESTful API for educational chatbot...",
  "endpoints": { ... },
  "usage_examples": { ... }
}
```

---

### 2. Health Check
**GET** `/api/health`

Check if the API is running and configured correctly.

**Authentication:** Not required

**Response:**
```json
{
  "status": "healthy",
  "gemini_configured": true,
  "model_initialized": true
}
```

---

### 3. Chat Endpoint
**POST** `/api/chat`

Send a message to the educational chatbot and get an AI-generated response.

**Authentication:** Required

**Request Body:**
```json
{
  "message": "What courses should I take for web development?"
}
```

**Response:**
```json
{
  "response": "For web development, I recommend starting with...",
  "timestamp": "2024-01-01T12:00:00"
}
```

**Error Responses:**
- `400` - Bad Request (missing or invalid message)
- `401` - Unauthorized (invalid or missing API key)
- `500` - Internal Server Error

---

### 4. List Models
**GET** `/api/models`

List all available Gemini models.

**Authentication:** Required

**Response:**
```json
{
  "available_models": [
    {
      "name": "models/gemini-2.5-flash",
      "display_name": "Gemini 2.5 Flash",
      "description": "Stable version of Gemini 2.5 Flash..."
    }
  ],
  "current_model": "genai.GenerativeModel(...)"
}
```

---

## Usage Examples

### cURL

```bash
# Health check
curl https://your-app-name.onrender.com/api/health

# Chat request
curl -X POST https://your-app-name.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key-here" \
  -d '{"message": "What is Python programming?"}'
```

### JavaScript (Fetch API)

```javascript
fetch('https://your-app-name.onrender.com/api/chat', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': 'your-api-key-here'
  },
  body: JSON.stringify({
    message: 'What courses should I take for data science?'
  })
})
.then(response => response.json())
.then(data => {
  console.log(data.response);
})
.catch(error => {
  console.error('Error:', error);
});
```

### Python (requests)

```python
import requests

response = requests.post(
    'https://your-app-name.onrender.com/api/chat',
    headers={
        'Content-Type': 'application/json',
        'X-API-Key': 'your-api-key-here'
    },
    json={
        'message': 'What skills do I need for machine learning?'
    }
)

data = response.json()
print(data['response'])
```

### React Example

```jsx
import React, { useState } from 'react';

function Chatbot() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const sendMessage = async () => {
    try {
      const res = await fetch('https://your-app-name.onrender.com/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-API-Key': 'your-api-key-here'
        },
        body: JSON.stringify({ message })
      });
      
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <input 
        value={message} 
        onChange={(e) => setMessage(e.target.value)} 
      />
      <button onClick={sendMessage}>Send</button>
      <div>{response}</div>
    </div>
  );
}
```

---

## Error Handling

All errors return JSON in the following format:

```json
{
  "error": "Error message here"
}
```

### Common Error Codes

- **400 Bad Request** - Invalid request body or missing required fields
- **401 Unauthorized** - Invalid or missing API key
- **500 Internal Server Error** - Server-side error

---

## Rate Limiting

Currently, there are no rate limits, but please use the API responsibly.

---

## Support

For issues or questions, contact your API administrator.

