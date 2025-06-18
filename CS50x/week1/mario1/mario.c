#include <cs50.h>
#include <stdio.h>

void print_row(int n);

int main(void)
{
    // Prompt user for input
    int n;

    do
    {
        n = get_int("Height: ");
        // Print n rows
        for (int row = 0; row < n; row++)
        {
            // Print x-spaces before the bricks
            // (n - 1) - row decreases number of spaces
            for (int spaces = (n - 1) - row; spaces > 0; spaces--)
            {
                printf("%c", ' ');
            }
            print_row(row + 1);
        }
    }
    while (n < 1);
}

void print_row(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");
}
