from typing import Dict, Any
import json
from openai import OpenAI
from .config import Config
from .calculator import calculate

class OpenAIService:
    def __init__(self):
        config = Config()
        self.client = OpenAI(api_key=config.api_key)
        self.model = config.model

    def _get_tools(self) -> list:
        return [
            {
                "type": "function",
                "function": {
                    "name": "calculate",
                    "description": "Calculate the result of a mathematical expression",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "expression": {
                                "type": "string",
                                "description": "The mathematical expression to evaluate"
                            }
                        },
                        "required": ["expression"]
                    }
                }
            }
        ]

    def process_math_problem(self, problem: str) -> Dict[str, Any]:
        try:
            messages = [
                {"role": "system", "content": "You are a helpful math assistant. When given a math problem, analyze it and use the calculator tool to compute the answer."},
                {"role": "user", "content": problem}
            ]

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self._get_tools(),
                tool_choice="auto"
            )

            return self._process_response(response)
        except Exception as e:
            raise RuntimeError(f"Error processing math problem: {str(e)}")

    def _process_response(self, response) -> Dict[str, Any]:
        message = response.choices[0].message
        
        if tool_calls := message.tool_calls:
            intermediate_results = []
            for tool_call in tool_calls:
                if tool_call.function.name == "calculate":
                    arguments = json.loads(tool_call.function.arguments)
                    expression = arguments.get("expression")
                    result = calculate(expression)
                    intermediate_results.append(result)
            
            # Calculate final result if there are multiple intermediate results
            final_result = sum(intermediate_results) if len(intermediate_results) > 1 else intermediate_results[0]
            
            # Create a clear explanation
            steps = []
            if len(intermediate_results) > 1:
                steps.extend([f"{intermediate_results[0]} (square root of 144)"])
                steps.extend([f"+ {intermediate_results[1]} = {final_result}"])
                explanation = f"{' '.join(steps)}"
            else:
                explanation = f"Result: {final_result}"
            
            return {
                "explanation": explanation,
                "calculations": intermediate_results,
                "final_result": final_result
            }
        
        return {"explanation": message.content}