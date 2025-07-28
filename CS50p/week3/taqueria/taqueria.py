def main():
    # Create menu for users
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    process_order(menu)


def process_order(menu):
    # Ask for item, output total
    total = 0
    while True:
        try:
            order = input("Item: ").casefold().title()
            total += float(menu[order])
            print(f"Total: ${total:.2f}")
        # User presses control + D to finish order (end the program)
        except EOFError:
            print()
            break
        # Reprompt if user inputs invalid menu item
        except KeyError:
            pass


main()