budget = int(input())
season = input()
numbers_of_fishermans = int(input())

colected_money = 0
boat_price = 0
if season == "Spring":
    boat_price = 3000
elif season == "Summer":
    boat_price = 4200
elif season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if numbers_of_fishermans <= 6:
    boat_price = boat_price * (1 - 10 / 100)
elif 7 <= numbers_of_fishermans <= 11:
    boat_price = boat_price * (1 - 15 / 100)
elif 12 <= numbers_of_fishermans:
    boat_price = boat_price * (1 - 25 / 100)

if (numbers_of_fishermans % 2 == 0) and (not season == "Autumn"):
    boat_price = boat_price * (1 - 5/100)
if budget > boat_price:
    left_money = budget - boat_price
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = boat_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")

