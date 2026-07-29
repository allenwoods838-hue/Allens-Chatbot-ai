import json

print("Allo 1.0 Fast 🤖")
print("Type 'exit' to quit")

responses = {
    "hello": "Hello! I am Allo 1.0 Fast.",
    "hi": "Hi! How can I help?",
    "name": "I am Allo AI Fast 1.0."
}

while True:
    user = input("You: ").lower()
    if user == "exit":
        break

    answer = "I am still learning."
    for key in responses:
        if key in user:
            answer = responses[key]
            break

    print("Allo:", answer)
