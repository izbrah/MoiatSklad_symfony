# • Пакет химикали - 5.80 лв.
#
# • Пакет маркери - 7.20 лв.
#
# • Препарат - 1.20 лв (за литър)
#
# Вход
#
# От конзолата се четат 4 числа:
#
# · Брой пакети химикали - цяло число в интервала [0...100]
#
# · Брой пакети маркери - цяло число в инт2
# ервала [0...100]
#
# · Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# · Процент намаление - цяло число в интервала [0...100]
# print(f'{num :.2f}')
pens = int(input())
markers = int(input())
cleaner = int(input())
discount = int(input())
price_pens = pens*5.80
price_markers = markers*7.2
price_cleaners = cleaner*1.2
final_price = (price_pens+price_markers+price_cleaners) -  (price_pens+price_markers+price_cleaners)*discount/100
print(final_price)
