def main():
    vending_machine(50)


def vending_machine(amount):
    # Only allow integers 25, 10, and 5
    # Deduct allowed coins
    # Repeat process until amount reaches 0
    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount -= coin
    else:
        # Display change
        print(f"Change Owed: {abs(amount)}")


main()
