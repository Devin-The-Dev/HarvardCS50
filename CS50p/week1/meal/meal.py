def main():
    hours, minutes = input("What time is it? ").split(":")
    floatNum = convert(hours, minutes)
    if (floatNum >= 7 and floatNum <= 8):
        print("breakfast time")
    elif (floatNum >= 12 and floatNum <= 13):
        print("lunch time")
    elif (floatNum >= 18 and floatNum <= 19):
        print("dinner time")


def convert(hours, minutes):
        return float(int(hours) + int(minutes) / 60)

if __name__ == "__main__":
    main()
