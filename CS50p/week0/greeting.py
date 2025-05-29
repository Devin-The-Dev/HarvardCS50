def greet(input):
    if "Hello" in input:
        return "Hello, there"
    else:
        return "I'm not sure what you mean"


greeting = greet("Hello, computer")
print(f"{greeting}. General Kenobi!")
