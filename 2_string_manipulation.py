# Reverse String
string = "abcdcba"
stringReversed = string[::-1]
print(stringReversed)

# Number of Vowels in a String
sumVowels = 0
for char in string:
    if char in "aeiou": sumVowels +=1

print(f"Sum of Vowels is: {sumVowels}")

# Paindrome Checker
print("Checking for Palindrome.")
if string == stringReversed: print(f"{string} is a palindrome.")
else: print(f"{string} is not a palindrome.")