def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #If d starts with $, then delete $
    if d.startswith("$"):
        newD = ''.join(d.rsplit("$"))
        return float(newD)
    else:
        #Else return amount
        return float(d)


def percent_to_float(p):
    #If p ends with %. then delete %
    if p.endswith("%"):
        newP = ''.join(p.split("%"))
        return float(newP) / 100
    else:
        #Else return percentage
        return float(p) / 100


main()