camel_case = input("camelCase: ")


def snake_case(name):
    new_string = ""
    for char in name:
        # Add lowercases
        if char.islower():
            new_string += char
        else:
            # Put underscore in front of uppercase
            # Set all characters to lowercase
            new_string += "_" + char.lower()
    return new_string


print(f"snake_case: {snake_case(camel_case)}")
