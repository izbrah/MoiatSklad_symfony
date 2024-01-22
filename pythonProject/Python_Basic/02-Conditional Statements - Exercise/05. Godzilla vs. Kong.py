budget = float(input())
statistician = int(input())
clothing_price = float(input())

decor = budget * 1/10
clothing_price = statistician * clothing_price
if statistician > 150:
    clothing_price = clothing_price * (1-0.1)
final_price = decor + clothing_price
if final_price > budget:
    print("Not enough money!")
    needed_money = final_price - budget
    print(f"Wingard needs {needed_money:.2f} leva more." )
else:
    print("Action!")
    needed_money = budget - final_price
    print(f"Wingard starts filming with {needed_money:.2f} leva left.")
