import sys

n = input('変換したい数字入れてね: ')

if not n.isdecimal():
    print("数字じゃないよ！")
    sys.exit()

n = int(n)

def convert_from10(n,base):
    result = ''

    while n > 0:
        result = str(n % base) + result
        n //= base

    return result

print(convert_from10(n,2))
print(convert_from10(n,3))
print(convert_from10(n,10))