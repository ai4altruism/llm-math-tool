# Secure Math Problem Solver

A Python application that demonstrates a fundamental pattern in LLM application development: secure function calling and mathematical computation. This project implements a production-ready math problem solving pipeline that combines the natural language understanding capabilities of GPT models with secure, sandboxed mathematical computation.

This application serves as an educational template and building block, designed to help developers understand:
* How to implement secure mathematical evaluation systems using restricted environments
* How to leverage OpenAI's function calling capabilities for structured operations
* Best practices for handling user input in mathematical contexts
* Clean architecture principles in AI-powered computational systems
* Practical patterns for secure AI application development

While focused in scope, this codebase reflects patterns that can be expanded into more sophisticated applications, such as:
* Enterprise-grade mathematical processing systems
* AI-powered scientific computing platforms
* Secure computation services with natural language interfaces
* Educational tools for mathematics
* Automated problem-solving systems with step-by-step explanations

The implementation showcases the integration of several key technologies and concepts:
* OpenAI's GPT models for natural language understanding
* Function calling for structured mathematical operations
* Secure evaluation environments for safe computation
* Environment-based configuration management
* Comprehensive testing practices

## Features

* Natural language processing of mathematical problems
* Secure mathematical expression evaluation
* Step-by-step solution explanations
* Support for complex mathematical functions
* Comprehensive security measures against code injection
* Environment-based configuration
* Extensive test coverage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/secure-math-solver.git
cd secure-math-solver
```

2. Install dependencies:
```bash
pip install -e .
```

3. Create a .env file with your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
GPT_MODEL=gpt-4  # optional, defaults to gpt-4
```

## Usage

From the command line:
```bash
python main.py "sqrt(144) + 10"
```

In your Python code:
```python
from math_service.openai_service import OpenAIService

service = OpenAIService()
result = service.process_math_problem("sqrt(144) + 10")
print(result["explanation"])
print(result["final_result"])
```

## Architecture

The application follows a clean architecture pattern with clear separation of concerns:

* `main.py`: Command-line interface
* `openai_service.py`: Core service for OpenAI integration
* `calculator.py`: Secure mathematical evaluation
* `config.py`: Configuration management
* `setup.py`: Package configuration
* `test_calculator.py`: Unit tests

## Security

Security is a primary focus of this application:
* Restricted evaluation environment for mathematical expressions
* Whitelisted mathematical operations
* Environment-based secret management
* Comprehensive input validation
* Protection against code injection

## Testing

Run the test suite:
```bash
pytest
```

The test suite covers:
* Basic arithmetic operations
* Mathematical functions
* Security measures
* Edge cases and error handling

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details. Copyright (C) 2025.

## Contact

For questions and support, please contact: team@ai4altruism.org

## Acknowledgments

* OpenAI for providing the GPT API
* The Python community for security best practices

## Citation

If you use this code in your research or project, please cite:

```bibtex
@software{secure_math_solver,
  title = {Secure Math Problem Solver},
  author = {AI4Altruism Team},
  year = {2025},
  url = {https://github.com/yourusername/secure-math-solver}
}
```
