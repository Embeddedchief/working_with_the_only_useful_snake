

import sys


# ------------------------------------------------------------
# Q11. firstword
# Write first_word(s) that returns the first word of the string
# followed by "\n". Words are separated by spaces. Ignore leading
# spaces. Empty string or only spaces -> "\n".
# first_word("  hello there") -> "hello\n"
# ------------------------------------------------------------
def first_word(s):
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    start = i
    while i < len(s) and s[i] != ' ':
        i += 1
    return s[start:i] + "\n"


# ------------------------------------------------------------
# Q12. findprevprime
# Write find_prev_prime(n) that returns the largest prime number
# less than or equal to n. If there is none, return 0.
# find_prev_prime(5) -> 5,  find_prev_prime(4) -> 3,  find_prev_prime(1) -> 0
# ------------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def find_prev_prime(n):
    while n >= 2:
        if is_prime(n):
            return n
        n -= 1
    return 0


# ------------------------------------------------------------
# Q13. lastword
# Write last_word(s) that returns the last word followed by "\n".
# Ignore trailing spaces. Empty string -> "\n".
# last_word("hello there   ") -> "there\n"
# ------------------------------------------------------------
def last_word(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    end = i
    while i >= 0 and s[i] != ' ':
        i -= 1
    return s[i + 1:end + 1] + "\n"


# ------------------------------------------------------------
# Q14. repeatalpha
# Write repeat_alpha(s) that repeats each letter by its position
# in the alphabet (a=1, b=2, c=3...). Uppercase works the same.
# Non-letters stay as they are.
# repeat_alpha("abc") -> "abbccc",  repeat_alpha("a1B") -> "a1BB"
# ------------------------------------------------------------
def repeat_alpha(s):
    res = ""
    for c in s:
        if 'a' <= c <= 'z':
            res += c * (ord(c) - ord('a') + 1)
        elif 'A' <= c <= 'Z':
            res += c * (ord(c) - ord('A') + 1)
        else:
            res += c
    return res


# ------------------------------------------------------------
# Q15. fromto
# Write from_to(f, t) that returns all numbers from f to t (counting
# up or down), each shown with 2 digits, separated by ", ", ending
# with "\n". If f or t is outside 0..99, return "Invalid\n".
# from_to(1, 4)  -> "01, 02, 03, 04\n"
# from_to(10, 8) -> "10, 09, 08\n"
# ------------------------------------------------------------
def from_to(f, t):
    if f < 0 or f > 99 or t < 0 or t > 99:
        return "Invalid\n"
    step = 1 if f <= t else -1
    parts = []
    for i in range(f, t + step, step):
        if i < 10:
            parts.append("0" + str(i))
        else:
            parts.append(str(i))
    return ", ".join(parts) + "\n"


# ------------------------------------------------------------
# Q16. iscapitalized
# Write is_capitalized(s) that returns True if every word starts
# with something that is NOT a lowercase letter. Empty -> False.
# is_capitalized("Hello World") -> True
# is_capitalized("Hello world") -> False
# is_capitalized("Hello 1world") -> True
# ------------------------------------------------------------
def is_capitalized(s):
    if s == "":
        return False
    for word in s.split():
        if 'a' <= word[0] <= 'z':
            return False
    return True


# ------------------------------------------------------------
# Q17. printmemory
# Write print_memory(arr) that takes a list of 10 numbers (0-255).
# Print each as 2-digit lowercase hex, 4 per line, separated by
# spaces. Then print one line of characters: printable ones
# (32 to 126) as themselves, others as ".".
# print_memory([104,101,108,108,111,16,21,42,0,0]) prints:
# 68 65 6c 6c
# 6f 10 15 2a
# 00 00
# hello..*..
# ------------------------------------------------------------
def print_memory(arr):
    hexes = []
    for b in arr:
        hexes.append(format(b, "02x"))
    for i in range(0, len(hexes), 4):
        print(" ".join(hexes[i:i + 4]))
    line = ""
    for b in arr:
        if 32 <= b <= 126:
            line += chr(b)
        else:
            line += "."
    print(line)


# ------------------------------------------------------------
# Q18. thirdtimeisacharm
# Write third_time_is_a_charm(s) that returns every 3rd character
# (3rd, 6th, 9th...) followed by "\n". Empty -> "\n".
# third_time_is_a_charm("123456789") -> "369\n"
# ------------------------------------------------------------
def third_time_is_a_charm(s):
    return s[2::3] + "\n"


# ------------------------------------------------------------
# Q19. weareunique
# Write we_are_unique(a, b) that returns how many different
# characters appear in only ONE of the two strings.
# If both strings are empty, return -1.
# we_are_unique("foo", "boo") -> 2   (f and b)
# we_are_unique("abc", "def") -> 6
# ------------------------------------------------------------
def we_are_unique(a, b):
    if a == "" and b == "":
        return -1
    count = 0
    for c in set(a):
        if c not in b:
            count += 1
    for c in set(b):
        if c not in a:
            count += 1
    return count


# ------------------------------------------------------------
# Q20. zipstring
# Write zip_string(s) that compresses repeated characters next to
# each other into count + character.
# zip_string("aaabbc") -> "3a2b1c",  zip_string("") -> ""
# ------------------------------------------------------------
def zip_string(s):
    if s == "":
        return ""
    res = ""
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            res += str(count) + s[i - 1]
            count = 1
    return res


# ------------------------------------------------------------
# Q21. canjump
# Write can_jump(arr) that takes a list of non-negative numbers.
# Start at index 0. Each value is how far you jump forward.
# Return True if you land exactly on the last index.
# Empty list -> False.
# can_jump([2, 3, 1, 1, 4]) -> True   (0 -> 2 -> 3 -> 4)
# can_jump([3, 2, 1, 0, 4]) -> False
# ------------------------------------------------------------
def can_jump(arr):
    if len(arr) == 0:
        return False
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 0:
            return False
        i += arr[i]
    return i == len(arr) - 1


# ------------------------------------------------------------
# Q22. concatslice
# Write concat_slice(a, b) that returns one list with a's items
# followed by b's items.
# concat_slice([1, 2], [3, 4]) -> [1, 2, 3, 4]
# ------------------------------------------------------------
def concat_slice(a, b):
    return a + b


# ------------------------------------------------------------
# Q23. concatalternate
# Write concat_alternate(a, b) that alternates items from a and b.
# When one list runs out, add the rest of the other.
# concat_alternate([1, 3, 5], [2, 4]) -> [1, 2, 3, 4, 5]
# ------------------------------------------------------------
def concat_alternate(a, b):
    res = []
    i = 0
    while i < len(a) or i < len(b):
        if i < len(a):
            res.append(a[i])
        if i < len(b):
            res.append(b[i])
        i += 1
    return res


# ------------------------------------------------------------
# Q24. revconcatalternate
# Write rev_concat_alternate(a, b): like Q23 but starting from the
# END of both lists, going backwards.
# rev_concat_alternate([1, 2, 3], [4, 5, 6]) -> [3, 6, 2, 5, 1, 4]
# ------------------------------------------------------------
def rev_concat_alternate(a, b):
    res = []
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 or j >= 0:
        if i >= 0:
            res.append(a[i])
            i -= 1
        if j >= 0:
            res.append(b[j])
            j -= 1
    return res


# ------------------------------------------------------------
# Q25. saveandmiss
# Write save_and_miss(s, n): keep n characters, skip n characters,
# keep n, skip n... If n <= 0, return s unchanged.
# save_and_miss("123456789", 3) -> "123789"
# save_and_miss("abcdefghij", 2) -> "abefij"
# ------------------------------------------------------------
def save_and_miss(s, n):
    if n <= 0:
        return s
    res = ""
    for i in range(len(s)):
        if (i // n) % 2 == 0:
            res += s[i]
    return res


# ------------------------------------------------------------
# Q26. fifthandskip
# Write fifth_and_skip(s): ignore spaces, take 5 characters, skip
# the 6th, take 5, skip 1... Join the groups with a space and end
# with "\n". Empty -> "\n". Fewer than 5 characters -> "Invalid Input\n".
# fifth_and_skip("abcdefghijklmnopqrstuwxyz") -> "abcde ghijk mnopq stuwx z\n"
# ------------------------------------------------------------
def fifth_and_skip(s):
    if s == "":
        return "\n"
    chars = s.replace(" ", "")
    if len(chars) < 5:
        return "Invalid Input\n"
    groups = []
    i = 0
    while i < len(chars):
        groups.append(chars[i:i + 5])
        i += 6
    return " ".join(groups) + "\n"


# ------------------------------------------------------------
# Q27. notdecimal
# Write not_decimal(s): if s is a decimal number, remove the dot and
# return it as a whole number (no leading zeros) + "\n".
# If s is not a number, return s unchanged + "\n". Empty -> "\n".
# not_decimal("0.1") -> "1\n",  not_decimal("174.2") -> "1742\n"
# not_decimal("hello") -> "hello\n"
# ------------------------------------------------------------
def not_decimal(s):
    if s == "":
        return "\n"
    try:
        float(s)
    except ValueError:
        return s + "\n"
    return str(int(s.replace(".", ""))) + "\n"


# ------------------------------------------------------------
# Q28. slice
# Write slice_list(a, start, end=None) that returns part of a list.
# Negative numbers count from the end. If the range is invalid
# (start after end), return None.
# a = ["coding", "algorithm", "ascii", "package", "golang"]
# slice_list(a, 1)      -> ["algorithm", "ascii", "package", "golang"]
# slice_list(a, 2, 4)   -> ["ascii", "package"]
# slice_list(a, -3)     -> ["ascii", "package", "golang"]
# slice_list(a, 2, 0)   -> None
# ------------------------------------------------------------
def slice_list(a, start, end=None):
    l = len(a)
    if start < 0:
        start = l + start
    if end is None:
        end = l
    elif end < 0:
        end = l + end
    if start < 0 or end > l or start > end:
        return None
    return a[start:end]


# ------------------------------------------------------------
# Q29. wordflip
# Write word_flip(s) that reverses the order of the words, with one
# space between them, ending with "\n".
# Empty string -> "Invalid Output\n".
# word_flip("First second last") -> "last second First\n"
# word_flip("  hello   world ")  -> "world hello\n"
# ------------------------------------------------------------
def word_flip(s):
    if s == "":
        return "Invalid Output\n"
    words = s.split()
    words.reverse()
    return " ".join(words) + "\n"


# ------------------------------------------------------------
# Q30. itoabase
# Write itoa_base(v, base) that converts integer v to a string in
# the given base (2 to 16), using uppercase letters for 10-15.
# itoa_base(10, 2) -> "1010",  itoa_base(255, 16) -> "FF"
# itoa_base(-15, 16) -> "-F"
# ------------------------------------------------------------
def itoa_base(v, base):
    digits = "0123456789ABCDEF"
    if v == 0:
        return "0"
    neg = v < 0
    if neg:
        v = -v
    res = ""
    while v > 0:
        res = digits[v % base] + res
        v = v // base
    if neg:
        res = "-" + res
    return res


# ------------------------------------------------------------
# Q31. chunk
# Write chunk(arr, size) that PRINTS the list split into smaller
# lists of length size (the last one may be shorter).
# If size is 0, print an empty line.
# chunk([1,2,3,4,5,6,7], 3) prints [[1, 2, 3], [4, 5, 6], [7]]
# ------------------------------------------------------------
def chunk(arr, size):
    if size == 0:
        print()
        return
    res = []
    for i in range(0, len(arr), size):
        res.append(arr[i:i + size])
    print(res)


# ============================================================
# PROGRAMS: they read command-line arguments and print.
# args = sys.argv[1:] (the words typed after the file name)
# ============================================================

# ------------------------------------------------------------
# Q32. addprimesum
# Program takes one positive number and prints the sum of all
# primes up to and including it. Wrong number of arguments or
# not a positive number -> print 0.
# python file.py 5   ->  10   (2 + 3 + 5)
# python file.py 7   ->  17
# ------------------------------------------------------------
def add_prime_sum(args):
    if len(args) != 1 or not args[0].isdigit():
        print(0)
        return
    n = int(args[0])
    total = 0
    for i in range(2, n + 1):
        if is_prime(i):       # is_prime is from Q12
            total += i
    print(total)


# ------------------------------------------------------------
# Q33. fprime
# Program takes one number and prints its prime factors in order,
# separated by "*". Wrong arguments or number <= 1 -> print nothing.
# python file.py 225225  ->  3*3*5*5*7*11*13
# python file.py 12      ->  2*2*3
# ------------------------------------------------------------
def fprime(args):
    if len(args) != 1:
        return
    try:
        n = int(args[0])
    except ValueError:
        return
    if n <= 1:
        return
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(str(i))
            n = n // i
        else:
            i += 1
    print("*".join(factors))


# ------------------------------------------------------------
# Q34. hiddenp
# Program takes two strings. Print 1 if all characters of the first
# appear in the second IN THE SAME ORDER (not necessarily next to
# each other), else 0. Empty first string -> 1.
# Wrong number of arguments -> print nothing.
# python file.py "fgex.;" "tyf34gdgf;'ektufjhgdgex.;.;rtjynur6"  -> 1
# python file.py "abc" "btarc"  -> 0
# ------------------------------------------------------------
def hiddenp(args):
    if len(args) != 2:
        return
    s1, s2 = args
    j = 0
    for c in s2:
        if j < len(s1) and c == s1[j]:
            j += 1
    if j == len(s1):
        print(1)
    else:
        print(0)


# ------------------------------------------------------------
# Q35. inter
# Program takes two strings. Print the characters that appear in
# BOTH, in the order of the first string, no duplicates.
# python file.py "padinton" "paqefwtdjetyiytjneytjoeyjnejeyj"  ->  padinto
# ------------------------------------------------------------
def inter(args):
    if len(args) != 2:
        return
    res = ""
    for c in args[0]:
        if c in args[1] and c not in res:
            res += c
    print(res)


# ------------------------------------------------------------
# Q36. union
# Program takes two strings. Print every character from both,
# first string then second, without duplicates.
# Wrong number of arguments -> print an empty line.
# python file.py "zpadinton" "paqefwtdjetyiytjneytjoeyjnejeyj"  ->  zpadintoqefwjy
# ------------------------------------------------------------
def union(args):
    if len(args) != 2:
        print()
        return
    res = ""
    for c in args[0] + args[1]:
        if c not in res:
            res += c
    print(res)


# ------------------------------------------------------------
# Q37. wdmatch
# Program takes two strings. If the first can be made from
# characters of the second IN ORDER, print the first string.
# Otherwise print nothing. (Same logic as Q34.)
# python file.py "faya" "fgvvfdxcacpolhyghbreda"  ->  faya
# python file.py "error" "rrerrrfiiljdfxjyuifrrvcoojh"  ->  (nothing)
# ------------------------------------------------------------
def wdmatch(args):
    if len(args) != 2:
        return
    a, b = args
    j = 0
    for c in b:
        if j < len(a) and c == a[j]:
            j += 1
    if j == len(a):
        print(a)


# ------------------------------------------------------------
# Q38. revwstr
# Program takes one string and prints its words in reverse order,
# separated by single spaces.
# python file.py "the time of contempt precedes that of indifference"
#   ->  indifference of that precedes contempt of time the
# ------------------------------------------------------------
def revwstr(args):
    if len(args) != 1:
        return
    words = args[0].split()
    words.reverse()
    print(" ".join(words))


# ------------------------------------------------------------
# Q39. rostring
# Program takes one string and moves the FIRST word to the END.
# Words separated by single spaces in the output.
# Wrong arguments or no words -> print an empty line.
# python file.py "abc   " -> abc
# python file.py "Que la      lumiere soit et la lumiere fut"
#   ->  la lumiere soit et la lumiere fut Que
# ------------------------------------------------------------
def rostring(args):
    if len(args) != 1:
        print()
        return
    words = args[0].split()
    if len(words) == 0:
        print()
        return
    words = words[1:] + [words[0]]
    print(" ".join(words))


# ------------------------------------------------------------
# Q40. piglatin
# Program takes one word.
# If it starts with a vowel: add "ay" to the end.
# Otherwise: move the letters before the first vowel to the end,
# then add "ay". If there are no vowels, print "No vowels".
# python file.py pig    ->  igpay
# python file.py is     ->  isay
# python file.py crunch ->  unchcray
# python file.py crnch  ->  No vowels
# ------------------------------------------------------------
def piglatin(args):
    if len(args) != 1 or args[0] == "":
        return
    s = args[0]
    vowels = "aeiouAEIOU"
    for i in range(len(s)):
        if s[i] in vowels:
            print(s[i:] + s[:i] + "ay")
            return
    print("No vowels")


# ------------------------------------------------------------
# Q41. brackets
# Program takes any number of strings. For each one, print "OK" if
# its brackets () [] {} are correctly opened and closed, else "Error".
# Other characters are ignored. No arguments -> print nothing.
# python file.py "(johndoe)" "([)]" "" "{2*[d - 3]/(12)}"
#   ->  OK / Error / OK / OK   (each on its own line)
# ------------------------------------------------------------
def brackets_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            if len(stack) == 0 or stack.pop() != pairs[c]:
                return False
    return len(stack) == 0


def brackets(args):
    for s in args:
        if brackets_valid(s):
            print("OK")
        else:
            print("Error")


# ------------------------------------------------------------
# Q42. rpncalc
# Program takes one string in Reverse Polish Notation (numbers
# first, then the operator) and prints the result.
# Operators: + - * / %. Invalid expression, wrong arguments or
# division by zero -> print "Error".
# python file.py "1 2 * 3 * 4 +"  ->  10
# python file.py "3 1 2 * * 4 %"  ->  2
# python file.py "1 2 3 4 +"      ->  Error
# ------------------------------------------------------------
def rpncalc(args):
    if len(args) != 1:
        print("Error")
        return
    stack = []
    for t in args[0].split():
        if t.lstrip("-").isdigit():
            stack.append(int(t))
            continue
        if t not in ["+", "-", "*", "/", "%"] or len(stack) < 2:
            print("Error")
            return
        b = stack.pop()
        a = stack.pop()
        if t == "+":
            stack.append(a + b)
        elif t == "-":
            stack.append(a - b)
        elif t == "*":
            stack.append(a * b)
        else:
            if b == 0:
                print("Error")
                return
            if t == "/":
                stack.append(int(a / b))   # rounds towards zero
            else:
                stack.append(a % b)
    if len(stack) != 1:
        print("Error")
        return
    print(stack[0])


# ------------------------------------------------------------
# Q43. brainfuck
# Program takes one string of Brainfuck code and runs it.
# Memory: 2048 bytes, all 0, pointer at 0.
#   >  move pointer right      <  move pointer left
#   +  add 1 to current byte   -  subtract 1
#   .  print current byte as a character
#   [  if current byte is 0, jump past the matching ]
#   ]  if current byte is not 0, jump back to the matching [
# Any other character is ignored.
# python file.py "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
#   ->  Hello World!
# ------------------------------------------------------------
def brainfuck(args):
    if len(args) != 1:
        return
    code = args[0]
    mem = [0] * 2048
    ptr = 0
    i = 0
    out = ""
    while i < len(code):
        c = code[i]
        if c == '>':
            ptr += 1
        elif c == '<':
            ptr -= 1
        elif c == '+':
            mem[ptr] = (mem[ptr] + 1) % 256
        elif c == '-':
            mem[ptr] = (mem[ptr] - 1) % 256
        elif c == '.':
            out += chr(mem[ptr])
        elif c == '[' and mem[ptr] == 0:
            depth = 1
            while depth > 0:
                i += 1
                if code[i] == '[':
                    depth += 1
                elif code[i] == ']':
                    depth -= 1
        elif c == ']' and mem[ptr] != 0:
            depth = 1
            while depth > 0:
                i -= 1
                if code[i] == ']':
                    depth += 1
                elif code[i] == '[':
                    depth -= 1
        i += 1
    print(out, end="")


# ------------------------------------------------------------
# Q44. grouping
# Program takes a pattern like "(word1|word2)" and a text. Print
# every word of the text that contains any of the pattern parts,
# numbered: "1: word". Punctuation is removed from the printed word.
# Invalid pattern or wrong arguments -> print nothing.
# python file.py "(a)" "I'm heavy, jumpsuit is on steady, Lighter when I'm lower, higher when I'm heavy"
#   ->  1: heavy
#       2: steady
#       3: heavy
# ------------------------------------------------------------
def grouping(args):
    if len(args) != 2:
        return
    p, text = args
    if len(p) < 3 or p[0] != '(' or p[-1] != ')':
        return
    parts = p[1:-1].split("|")
    count = 1
    for w in text.split():
        clean = ""
        for c in w:
            if c.isalnum():
                clean += c
        for part in parts:
            if part != "" and part in w:
                print(str(count) + ": " + clean)
                count += 1
                break


# ============================================================
# QUICK TESTS: run this file to check everything works
#   python exam_practice_q11_to_q44.py
# ============================================================
if __name__ == "__main__":
    print(repr(first_word("  hello there")))         # 'hello\n'
    print(find_prev_prime(4))                        # 3
    print(repr(last_word("hello there   ")))         # 'there\n'
    print(repeat_alpha("abc"))                       # abbccc
    print(repr(from_to(10, 8)))                      # '10, 09, 08\n'
    print(is_capitalized("Hello world"))             # False
    print_memory([104, 101, 108, 108, 111, 16, 21, 42, 0, 0])
    print(repr(third_time_is_a_charm("123456789")))  # '369\n'
    print(we_are_unique("foo", "boo"))               # 2
    print(zip_string("aaabbc"))                      # 3a2b1c
    print(can_jump([2, 3, 1, 1, 4]))                 # True
    print(concat_alternate([1, 3, 5], [2, 4]))       # [1, 2, 3, 4, 5]
    print(rev_concat_alternate([1, 2, 3], [4, 5, 6]))  # [3, 6, 2, 5, 1, 4]
    print(save_and_miss("123456789", 3))             # 123789
    print(repr(fifth_and_skip("abcdefghijklmnopqrstuwxyz")))
    print(repr(not_decimal("0.1")))                  # '1\n'
    print(slice_list(["a", "b", "c", "d", "e"], -3)) # ['c', 'd', 'e']
    print(repr(word_flip("  hello   world ")))       # 'world hello\n'
    print(itoa_base(255, 16))                        # FF
    chunk([1, 2, 3, 4, 5, 6, 7], 3)
    add_prime_sum(["5"])                             # 10
    fprime(["225225"])                               # 3*3*5*5*7*11*13
    hiddenp(["abc", "btarc"])                        # 0
    inter(["padinton", "paqefwtdjetyiytjneytjoeyjnejeyj"])  # padinto
    union(["zpadinton", "paqefwtdjetyiytjneytjoeyjnejeyj"]) # zpadintoqefwjy
    wdmatch(["faya", "fgvvfdxcacpolhyghbreda"])      # faya
    revwstr(["the time of contempt"])                # contempt of time the
    rostring(["Que la      lumiere soit"])           # la lumiere soit Que
    piglatin(["crunch"])                             # unchcray
    brackets(["(johndoe)", "([)]", "", "{2*[d - 3]/(12)}"])
    rpncalc(["1 2 * 3 * 4 +"])                       # 10
    brainfuck(["++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."])
    grouping(["(a)", "I'm heavy, jumpsuit is on steady, Lighter when I'm lower, higher when I'm heavy"])