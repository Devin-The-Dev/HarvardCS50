# Only remove vowels from a string
def main():
    text = input("Input: ")
    print(f"Output: {consonants(text)}")

# Display consonants only
def consonants(word):
    new_string = ""
    for char in word:
        match char:
            # Skip vowels
            case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
                continue
            # Append consonants
            case _:
                new_string += char
    return new_string


main()