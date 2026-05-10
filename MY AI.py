import json
import os

FILE_NAME = "brain.json"

# Load existing memory
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        brain = json.load(file)
else:
    brain = {
        "hello": "Hi!",
        "how are you": "I am fine",
        "bye": "Goodbye!"
    }

print("=== Self-Learning Chat Bot ===")
print("Type 'bye' to exit\n")

while True:
    user = input("You: ").lower().strip()

    if user == "bye":
        print("AI : Goodbye!")
        break

    # If known question
    if user in brain:
        print("AI :", brain[user])

    # If unknown question → learn it
    else:
        print("Bot: I don't know this. Teach me!")
        answer = input("Enter correct answer: ")

        brain[user] = answer

        # Save updated memory
        with open(FILE_NAME, "w") as file:
            json.dump(brain, file, indent=4)

        print("Bot: Thanks! I learned something new.")