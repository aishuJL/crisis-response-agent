# main.py

from src.planner import plan_response
from src.executor import execute

def main():
    print("Welcome to Crisis Response Agent \n")
    emergency_type = input("Enter emergency type (fire, flood, earthquake, etc.): ")
    user_message = input("Describe your emergency: ")

    prompt = plan_response(emergency_type, user_message)
    response = execute(prompt)

    print("\n AI-Powered Response:\n")
    print(response)

if __name__ == "__main__":
    main()
