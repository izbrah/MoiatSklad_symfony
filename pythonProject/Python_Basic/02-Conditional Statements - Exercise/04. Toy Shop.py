excursion_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle = puzzle_count*2.6
dolls = dolls_count * 3
bears = bears_count * 4.1
mininon = minions_count * 8.2
trucks = trucks_count * 2

purchases = puzzle + dolls + bears + mininon + trucks
discount_purchases = purchases * (1-0.25)
sum_of_purchases = (puzzle_count
                    + dolls_count
                    + bears_count
                    + minions_count
                    + trucks_count)
if sum_of_purchases >= 50:
    profit = discount_purchases
else:
    profit = purchases

profit = profit * (1-0.1)
if profit >= excursion_price:
    left_money = profit - excursion_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    shortage = excursion_price - profit
    print(f"Not enough money! {shortage:.2f} lv needed.")
