class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    @staticmethod
    def evaluate(expression: str) -> float:
        """Evaluate a simple arithmetic expression."""
        try:
            # Basic safety check - only allow numbers and basic operators
            allowed_chars = set('0123456789+-*/(). ')
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")
            
            # Use eval with a restricted environment
            return eval(expression, {"__builtins__": {}}, {})
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {str(e)}") 