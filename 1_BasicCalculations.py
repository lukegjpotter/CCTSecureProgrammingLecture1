# Triangle Area
def triangleAreaCalculator(base, height):
    return base * height / 2

print(f"Area of Triangle is: {triangleAreaCalculator(5, 10)}")

# Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C is {fahrenheit}°F")

celsiusToFahrenheit(0)
celsiusToFahrenheit(38)

# Loan Interest
principle = 100000
interestRate = 0.6
periodInYears = 5
simpleInterest = (principle * interestRate * periodInYears) / 100
print(f"Simple Interest is: €{simpleInterest}")