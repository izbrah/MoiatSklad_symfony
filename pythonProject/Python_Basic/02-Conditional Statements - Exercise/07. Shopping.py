budget = float(input())
videocard_number = int(input())
procesors_number = int(input())
ram_number = int(input())

videocard_price = videocard_number * 250
procesors_price = videocard_price * 0.35 * procesors_number
ram_price = videocard_price * 0.1 * ram_number
shopping_price = videocard_price + procesors_price + ram_price
if videocard_number > procesors_number:
    shopping_price = shopping_price * (1-0.15)
if budget >= shopping_price:
    left = budget - shopping_price
    print(f"You have {left:.2f} leva left!" )
else:
    left = shopping_price - budget
    print(f"Not enough money! You need {left:.2f} leva more!")

