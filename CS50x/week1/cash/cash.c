#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Print amount of coins; specification not required
    int money;
    int coins = 0;

    // Ask "change owed", repeat if input < 0
    do
    {
        money = get_int("Change owed: ");

        // Count number of coins, repeat until money == 0
        do
        {
            // Quaters
            if (money >= 25)
            {
                coins++;
                money -= 25;
            }
            // Dimes
            else if (money >= 10)
            {
                coins++;
                money -= 10;
            }
            // Nickles
            else if (money >= 5)
            {
                coins++;
                money -= 5;
            }
            // Pennies
            else if (money >= 1)
            {
                coins++;
                money -= 1;
            }
        }
        while (money > 0);
    }
    while (money < 0);

    // Print number of coins
    printf("%d\n", coins);
}
