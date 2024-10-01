userInput = str(input("Enter a string: "))
longestSentence = ""

while True: 

    if len(userInput) > len(longestSentence):
        longestSentence = userInput

    if userInput.startswith("A"):
        print("Longest was: ", longestSentence)
        break

    else:
        userInput = str(input("Enter a string: "))
