# src/planner.py

from prompts import response_template

def plan_response(emergency_type, user_message):
    prompt = response_template.format(
        emergency_type=emergency_type,
        user_message=user_message
    )
    return prompt
