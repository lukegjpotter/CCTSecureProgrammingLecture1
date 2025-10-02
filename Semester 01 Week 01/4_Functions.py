# Write a function with a Default Argument
def power(base, exponent=2):
    try:
        return int(base) ** int(exponent)
    except ValueError:
        print("The base and exponent must be an integer.")

print(f"{power(3)}")
print(f"{power(4, 3)}")
print(f"{power(3.4)}")


# Return multiple values from function
def minMax(numbers):
    minValue = min(numbers)
    maxValue = max(numbers)
    return minValue, maxValue

numbers = [69, 100, 420]
min, max = minMax(numbers)
print(f"Min: {min}. Max: {max}. Source: {numbers}.")

# Nested function calls
def isEven(number):
    return number % 2 == 0

def printEvenOrOdd(number):
    if isEven(number): print("Even")
    else: print("Odd")

printEvenOrOdd(69)
printEvenOrOdd(100)