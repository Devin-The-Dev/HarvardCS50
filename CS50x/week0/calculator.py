def main():
    x = int(input("What's x? "))
    print(f"x^2 is {square(x)}")


def square(n):
    return pow(n, 2)


main()