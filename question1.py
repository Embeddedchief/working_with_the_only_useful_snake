#Write a program that checks a string and returns True if it contains digit, false if otherwise

def check_digit(s : str) -> bool:
    for c in s:
        if c.isdigit():
            return True
    return False

word = input('give me a word to check: ')
print(check_digit(word))

