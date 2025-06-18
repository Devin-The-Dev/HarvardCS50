def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Has max of 6 characters
    # Has min of 2 characters
    # String does not have special characters
    if (len(s) > 1 and len(s) < 7 and s.isalnum()):
        alpha_substring = ""
        num_substring = ""
        # First 2 characters in string are in the alphabet
        if (s[:2].isalpha()):
            # Separate letters and digits
            for char in s:
                if (char.isalpha()):
                    alpha_substring += char
                else:
                    num_substring += char
        else:
            return False
        # Number substring should NOT start with 0
        # Substring should NOT match end of string
        if not (s.endswith(num_substring)):
            return False
        elif (num_substring.startswith("0")):
            return False
        else:
            return True
    # Special characters return False
    else:
        return False


main()
