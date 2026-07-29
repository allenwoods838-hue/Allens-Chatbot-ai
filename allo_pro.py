import random

print("Allo 1.0 Pro 🧠")
print("Type 'exit' to quit")

knowledge = {
    "hello": ["Hello!", "Hi there!"],
    "python": ["Python is a programming language."],
    "ai": ["AI allows computers to learn patterns from data."]
}

while True:
    text = input("You: ").lower()

    if text == "exit":
        break

    reply = "I don't know that yet, but I can learn!"

    for topic, answers in knowledge.items():
        if topic in text:
            reply = random.choice(answers)
            break

    print("Allo Pro:", reply)
