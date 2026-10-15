#Write a program that takes a string and returns how many letters (a to z and A to Z) it contains. Digits, spaces, and symbols don’t count

def count_alpha(s: str) -> int:
    n = 0
    for c in s:
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
            n += 1
    return n

word = input('enter the word to count: ')
print(count_alpha(word))