import random

QUOTES = [
    "Stay hungry, stay foolish. – Steve Jobs",
    "Simplicity is the soul of efficiency. – Austin Freeman",
    "It always seems impossible until it's done. – Nelson Mandela",
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Make it work, make it right, make it fast. – Kent Beck",
    "There is no place like 127.0.0.1",
    "I'm not lazy, I'm in energy-saving mode. – Every developer ever",
]

def get_quote():
    return random.choice(QUOTES)
