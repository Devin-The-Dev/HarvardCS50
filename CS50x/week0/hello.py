def main():
    name = input("What's your name? ")
    hello(' '.join(name.strip().title().split()))


def hello(to="world"):
    print(f"Hello, {to}")

main()