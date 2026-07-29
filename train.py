import json

print("Allo AI Training Script")
print("Loading training data...")

with open("train_data.json", "r") as file:
    data = json.load(file)

intents = data["intents"]

print(f"Loaded {len(intents)} intents")

for intent in intents:
    print("Training:", intent["tag"])
    print("Examples:", len(intent["patterns"]))

print("Training complete! Allo model data is ready.")

# Future upgrades:
# - Add TensorFlow neural network training
# - Save model weights
# - Add tokenizer
