#Write a function that print more than 3 if word is more than 3
def counter(s : str) -> int:
    if len(s) > 3:
        return "Greater than 3"
    elif len(s) == 3:
        return "same"
    elif len(s) == "":
        return "invalid"
    else:
        return "less than 3"

word = input('Enter the word: ')

print(counter(word))