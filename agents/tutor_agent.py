import google.generativeai as genai
from .math_agent import MathAgent
from .physics_agent import PhysicsAgent

class TutorAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.math_agent = MathAgent(api_key)
        self.physics_agent = PhysicsAgent(api_key)
    
    async def process_query(self, query: str) -> str:
        """Process a query and delegate to appropriate specialist agent."""
        try:
            # Use Gemini to classify the query
            classification_prompt = f"""Classify this question as either 'math' or 'physics':
            Question: {query}
            Respond with only one word: 'math' or 'physics'"""
            
            response = self.model.generate_content(classification_prompt)
            subject = response.text.strip().lower()
            
            # Delegate to appropriate agent
            if subject == 'math':
                return await self.math_agent.process_query(query)
            elif subject == 'physics':
                return await self.physics_agent.process_query(query)
            else:
                return "I'm not sure if this is a math or physics question. Could you please rephrase it?"
                
        except Exception as e:
            return f"I encountered an error while processing your question: {str(e)}" 