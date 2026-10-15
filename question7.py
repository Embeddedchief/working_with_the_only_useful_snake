#greatest common divisor

def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input('input a: '))
b = int(input('input b: '))

print(greatest_common_divisor(a, b))