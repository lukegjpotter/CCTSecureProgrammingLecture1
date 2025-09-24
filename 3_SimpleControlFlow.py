# Even or Odd
def evenOrOdd(number):
    result = "odd"
    if number % 2 == 0: result = "even"
    print(f"The number {number} is {result}.")

evenOrOdd(3)
evenOrOdd(4)

# Print largest number
numbers = [1, 2, 3, 4, 5]
print(f"Largest number of {numbers} is {max(numbers)}")

# Leap Year Checker
def leapYearChecker(year):
    result = "not a leap year"
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: result = "a leap year"
    print(f"The year {year} is {result}.")

leapYearChecker(2000)
leapYearChecker(2001)