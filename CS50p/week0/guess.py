def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

def main():
    guess = get_guess()
    if guess == 5:
        print("Correct!")
    else:
        print("Incorrect!")


main()
