import sys

def mohu(n):
    hoge = n + "もっふもふ"
    return hoge

def huwa(n):
    hoge = n + "ふわふわ"
    return hoge

n1 = input('もふもふにしたい人の名前を入力してね: ')
n2 = input('ふわふわにしたい人の名前を入力してね: ')

if n1.isdecimal():
    print("stringで入力してください")
    sys.exit()

if n2.isdecimal():
    print("stringで入力してください")
    sys.exit()

result1 = mohu(n1)
result2 = huwa(n2)

print(result1)
print(result2)