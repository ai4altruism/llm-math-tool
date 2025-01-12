from setuptools import setup, find_packages

setup(
    name="math_service",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-dotenv>=0.19.0",
        "openai>=1.0.0",
    ],
    python_requires=">=3.7",
)