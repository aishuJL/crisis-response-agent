# src/executor.py

from src.gemini_client import generate_content

def execute(prompt):
    return generate_content(prompt)
