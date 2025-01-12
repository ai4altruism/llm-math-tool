import math

def calculate(expression: str) -> float:
    """
    Safely evaluate a mathematical expression.
    """
    # Create a safe dictionary of allowed mathematical operations
    safe_dict = {
        'abs': abs, 'max': max, 'min': min,
        'round': round, 'sum': sum,
        'pow': pow, 'sqrt': math.sqrt,
        'pi': math.pi, 'e': math.e
    }
    
    try:
        # Evaluate the expression in a restricted environment
        return float(eval(expression, {"__builtins__": {}}, safe_dict))
    except Exception as e:
        raise ValueError(f"Invalid mathematical expression: {str(e)}")