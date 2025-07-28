def main():
    # Store grocereis in empty dictionary
    grocery_dict = {}

    # Have user to keep adding groceries
    while True:
        try:
            item = input("").upper()
            if item in grocery_dict:
                grocery_dict[item] += 1
            else:
                grocery_dict[item] = 1
        # Exit on EOFError - control + D
        except EOFError:
            print()
            break

    alphabetize(grocery_dict)


def alphabetize(dictionary):
    # Sort keys into a list
    sorted_keys = sorted(dictionary.keys())

    for key in sorted_keys:
        print(f"{dictionary[key]} {key}")


main()