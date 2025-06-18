#Patterns - input: int(), output: float(), only 1 operation, include negatives
x, y, z = input("Expression: ").split()

def operator(num1, symbol, num2):
    a = int(num1)
    b = int(num2)

    # Common operators
    match symbol:
        case "+":
            return float(a + b)
        case "-":
            return float(a - b)
        case "*":
            return float(a * b)
        case "/":
            return float(a / b)
        case "%":
            return float(a % b)
        case "^":
            return float(pow(a, b))
        case _:
            return "Unknown expression"

print(operator(x, y, z))
