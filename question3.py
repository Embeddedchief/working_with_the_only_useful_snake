#Write a program count_char(s, c) that takes a string s and a single character c, and returns how many times c appears in s

#def count_char(s, c):
    #return s.count(c)

def count_char(word, c):
    n = 0
    for ch in word:
        if ch == c:
            n += 1
    return n

word = input('type the word: ')
c = input('type the char: ')

print(count_char(word, c))