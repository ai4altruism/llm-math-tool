#!/usr/bin/env python3
import argparse
from math_service.openai_service import OpenAIService

def main():
    parser = argparse.ArgumentParser(description='Solve math problems using OpenAI API')
    parser.add_argument('problem', type=str, help='The math problem to solve')
    args = parser.parse_args()

    service = OpenAIService()
    try:
        result = service.process_math_problem(args.problem)
        print("\nStep by step:", result["explanation"])
        if "final_result" in result:
            print(f"Final answer: {result['final_result']}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()