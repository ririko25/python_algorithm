import sys

n = input('もふもふにしたい人の名前を入力してね: ')

if n.isdecimal():
    print("stringで入力してください")
    sys.exit()


def mohu(n):
    hoge = n + "もっふもふ"
    return hoge

result = mohu(n)

print(result)
 