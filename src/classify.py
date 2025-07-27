def classify_emergency(user_message):
    message = user_message.lower()
    if any(keyword in message for keyword in ["fire", "smoke", "burn", "flame"]):
        return "Fire"
    elif any(keyword in message for keyword in ["flood", "water rising", "drowning"]):
        return "Flood"
    elif any(keyword in message for keyword in ["earthquake", "tremor", "shaking"]):
        return "Earthquake"
    else:
        return "General Emergency"
