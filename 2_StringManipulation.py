def stringManipulation(string):
    print(f"Input is: {string}")
    # Reverse String
    stringReversed = string[::-1]
    print(f"Reversed: {stringReversed}")

    # Number of Vowels in a String
    sumVowels = 0
    for char in string:
        if char in "aeiou": sumVowels +=1

    print(f"Sum of Vowels is: {sumVowels}")

    # Paindrome Checker
    if string == stringReversed: print(f"{string} is a palindrome.")
    else: print(f"{string} is not a palindrome.")

    print("\n  ---  \n")

stringManipulation("abcdcba")
stringManipulation("Luke likes Manga")