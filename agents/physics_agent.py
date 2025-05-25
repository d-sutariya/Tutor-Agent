import google.generativeai as genai
from tools.physics_constants import PhysicsConstants
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

class PhysicsAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.constants = PhysicsConstants()
        print("Physics agent initialized")
    
    async def process_query(self, query: str) -> str:
        """Process a physics-related query."""
        try:
            # Check if the query is about a physics constant
            constant_info = self._extract_constant_query(query)
            if constant_info:
                return constant_info
            print(f"Processing Physics query: {query}")
            # For other physics questions, use Gemini
            response = self.model.generate_content(
                f"""You are a physics tutor. Please help with this question: {query}
                Provide a clear, step-by-step explanation if it's a problem-solving question.
                For conceptual questions, provide a concise but comprehensive explanation.
                Include relevant formulas and units in your explanation."""
            )
            return response.text
        except Exception as e:
            return f"I encountered an error while processing your question: {str(e)}"
    
    def _extract_constant_query(self, query: str) -> str:
        """Extract and respond to queries about physics constants."""
        query = query.lower()
        
        # Check if it's a request to list all constants
        if any(phrase in query for phrase in ['list constants', 'show constants', 'what constants']):
            constants = self.constants.list_constants()
            return "Available physics constants:\n" + "\n".join(f"- {c}" for c in constants)
        
        # Check for specific constant queries
        for constant in self.constants.list_constants():
            if constant.replace('_', ' ') in query:
                value, unit = self.constants.get_constant_with_unit(constant)
                return f"The {constant.replace('_', ' ')} is {value} {unit}"
        
        return None 