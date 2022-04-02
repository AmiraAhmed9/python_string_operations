txt = "Be who you are and say what you feel"     #question1
print(txt.count("you"))


def palindrome(string):     #question3
    i=0
    for i in range(len(string)//2):
        print(string[i],string[(len(string) - 1) - i])
    if string[i] != string[(len(string) - 1) - i]:
            return "Given text is not Palindrome"
    i += 1
    return "Given text is  Palindrome"

text=input("Plz Enter text ")
print( palindrome(text))
