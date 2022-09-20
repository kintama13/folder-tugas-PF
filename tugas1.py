def sum_squares(*angka):
    a = [*angka]
    b = 0
    for c in a:
        b += c**2
    return b

print(sum_squares(1, 2, 3))

def triangle(a):
    b = a
    if a < 0:
        return "hanya menerima angka positif"
    while a != 0:
        a -= 1
        b+=a
    return b

print(triangle(5))

def square(x, y):
    z = x
    if x < 0 or y < 0:
        return "hanya menerima angka positif"
    if y==0:
        return 1
    selesai = 0
    while selesai < y - 1:
        x = x * z
        selesai += 1
    return x

print(square(3, 2))

def palindrome(I):
    return I == I[::-1]

print(palindrome("rotator"))