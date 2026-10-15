#Write a function rect_perimeter(w, h) that takes the width and height of a rectangle and returns its perimeter. If either w or h is negative, return -1

def calc_perimeter(w : int, h : int) -> int:
    if w < 0 or h < 0:
        return -1
    return 2 * (w + h)

width = int(input('Enter the width: '))
height = int(input('Enter the height: '))

print(calc_perimeter(width, height))