import sys

insert_price = input('insert: ')

if not insert_price.isdecimal():
    print("数字じゃないよ！")
    sys.exit()

product_price = input('product: ')

if not product_price.isdecimal():
    print("数字じゃないよ！")
    sys.exit()

change = int(insert_price) - int(product_price)

if change < 0:
    print("たりてないよ")
    sys.exit()

coin = [5000, 1000, 500, 100, 50, 10 ,1]

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ': ' + str(r))

