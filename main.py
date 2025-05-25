import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
from agents.tutor_agent import TutorAgent

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Multi-Agent Tutoring System")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize tutor agent
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

tutor_agent = TutorAgent(api_key)

class Query(BaseModel):
    query: str

@app.get("/", response_class=HTMLResponse)
async def get_home():
    """Serve the home page."""
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Multi-Agent Tutoring System</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <div class="container">
                <h1>Multi-Agent Tutoring System</h1>
                <div class="chat-container">
                    <div id="chat-messages"></div>
                    <div class="input-container">
                        <input type="text" id="query-input" placeholder="Ask a math or physics question...">
                        <button onclick="sendQuery()">Send</button>
                    </div>
                </div>
            </div>
            <script>
                async function sendQuery() {
                    const input = document.getElementById('query-input');
                    const query = input.value.trim();
                    if (!query) return;

                    // Add user message
                    addMessage('You: ' + query, 'user-message');
                    input.value = '';

                    try {
                        const response = await fetch('/api/query', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ query: query }),
                        });
                        const data = await response.json();
                        addMessage('Tutor: ' + data.response, 'tutor-message');
                    } catch (error) {
                        addMessage('Error: Failed to get response', 'error-message');
                    }
                }

                function addMessage(text, className) {
                    const messages = document.getElementById('chat-messages');
                    const message = document.createElement('div');
                    message.className = 'message ' + className;
                    message.textContent = text;
                    messages.appendChild(message);
                    messages.scrollTop = messages.scrollHeight;
                }

                // Allow Enter key to send message
                document.getElementById('query-input').addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        sendQuery();
                    }
                });
            </script>
        </body>
    </html>
    """

@app.post("/api/query")
async def process_query(query: Query):
    """Process a query through the tutoring system."""
    try:
        response = await tutor_agent.process_query(query.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 