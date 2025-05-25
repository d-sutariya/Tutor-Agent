# Multi-Agent Tutoring System

This project implements a multi-agent tutoring system that uses Google's Gemini API to provide specialized tutoring in mathematics and physics. The system consists of a main Tutor Agent that delegates queries to specialized sub-agents based on the subject matter.

## Architecture

The system follows a multi-agent architecture with the following components:

1. **Tutor Agent (Main Agent)**
   - Primary interface for user interaction
   - Handles query classification and delegation
   - Orchestrates communication between sub-agents

2. **Specialist Agents**
   - Math Agent: Handles mathematics-related queries
   - Physics Agent: Handles physics-related queries
   - Each agent has specialized tools and knowledge

3. **Tools**
   - Math Agent: Calculator tool for basic arithmetic operations
   - Physics Agent: Constants lookup tool for physics formulas

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

4. Run the application locally:
```bash
uvicorn main:app --reload
```

5. Access the application at `http://localhost:8000`

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .env
├── main.py
├── agents/
│   ├── __init__.py
│   ├── tutor_agent.py
│   ├── math_agent.py
│   └── physics_agent.py
├── tools/
│   ├── __init__.py
│   ├── calculator.py
│   └── physics_constants.py
└── static/
    └── style.css
```

## API Endpoints

- `POST /api/query`: Submit a question to the tutoring system
  - Request body: `{"query": "your question here"}`
  - Response: `{"response": "agent's response"}`

## Live Demo

[Link to deployed application]

## Implementation Details

The system uses Google's Gemini API for natural language understanding and response generation. The Tutor Agent uses simple keyword matching to determine which specialist agent should handle the query. Each specialist agent has access to specific tools that help them provide accurate responses.

### Challenges and Solutions

1. **Query Classification**: Implemented a simple keyword-based classification system that can be enhanced with more sophisticated NLP techniques.
2. **Tool Integration**: Created modular tool implementations that can be easily extended with new functionality.
3. **Error Handling**: Implemented comprehensive error handling for API calls and tool operations.

## Contributing

Feel free to submit issues and enhancement requests! 