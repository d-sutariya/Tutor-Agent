import google.generativeai as genai
from tools.calculator import Calculator

class MathAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.calculator = Calculator()
    
    async def process_query(self, query: str) -> str:
        """Process a mathematics-related query."""
        try:
            print(f"Processing Math query: {query}")
            # Check if the query contains a calculation
            if any(op in query for op in ['+', '-', '*', '/', '=']):
                # Extract the calculation part
                calculation = self._extract_calculation(query)
                if calculation:
                    result = self.calculator.evaluate(calculation)
                    return f"The result of {calculation} is {result}"
            
            # If no direct calculation or for conceptual questions, use Gemini
            response = self.model.generate_content(
                f"""You are a mathematics tutor. Please help with this question: {query}
                Provide a clear, step-by-step explanation if it's a problem-solving question.
                For conceptual questions, provide a concise but comprehensive explanation."""
            )
            return response.text
        except Exception as e:
            return f"I encountered an error while processing your question: {str(e)}"
    
    def _extract_calculation(self, query: str) -> str:
        """Extract a calculation expression from the query."""
        # This is a simple implementation - could be enhanced with more sophisticated parsing
        import re
        # Look for patterns like "calculate 2 + 3" or "what is 2 + 3"
        calc_pattern = r'(?:calculate|what is|solve|compute)\s+([\d\s\+\-\*\/\(\)\.]+)'
        match = re.search(calc_pattern, query.lower())
        if match:
            return match.group(1).strip()
        return None 