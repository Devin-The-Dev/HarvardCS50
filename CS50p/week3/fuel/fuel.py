# Use datetime module for ease and lower memory use
from datetime import datetime


def main():
    # Convert middle endian format to iso8601 format
    print(middle_endian_to_iso8601("Date: "))


def middle_endian_to_iso8601(prompt):
    while True:
        # Ask user for date
        date = input(prompt).strip()

        try:
            # Check if the month is a number or spelled out
            if date[0].isdigit():
                dt_object = datetime.strptime(date, '%m/%d/%Y')
                return dt_object.strftime('%Y-%m-%d')
            elif date[0].isalpha():
                dt_object = datetime.strptime(date, '%B %d, %Y')
                return dt_object.strftime('%Y-%m-%d')
            else:
                raise ValueError
        except (TypeError, ValueError):
            pass


main()
