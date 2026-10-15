#write a function that cuts a string in half and print the remaining half

def retain_first_half(word : str) -> int:
    if len(word) == 1:
        return word
    return word [: len(word) // 2]

word = input('enter the word: ')

print(retain_first_half(word))