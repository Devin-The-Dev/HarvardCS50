# Get user input
# Set letters to lowercase and strip spaces for easier conditionals
greeting = input("Greeting: ").lower().strip(" ")

# We're only interested in the first word of the inital greeting
if (greeting.startswith("hello")):
    print("$0")
elif (greeting.startswith("h")):
    print("$20")
else:
    print("$100")
