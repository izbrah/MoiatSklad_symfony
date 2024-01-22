flower_kind = input()
number = int(input())
budget = int(input())

price = 0

if flower_kind == "Roses":
    if number > 80:
        price = number * 5 * (1-10/100)
    else:
        price = number * 5
elif flower_kind == "Dahlias":
    if number > 90:
        price = number * 3.8 * (1 - 15/100)
    else:
        price = number * 3.8
elif flower_kind == "Tulips":
    if number > 80:
        price = number * 2.8 * (1 - 15/100)
    else:
        price = number * 2.8
elif flower_kind == "Narcissus":
    if number < 120:
        price = number * 3 * (1 + 15/100)
    else:
        price = number * 3
elif flower_kind == "Gladiolus":
    if number < 80:
        price = number * 2.5 * (1 + 20/100)
    else:
        price = number * 2.5
if price <= budget:
    rest_money = budget - price
    print(f"Hey, you have a great garden with {number} {flower_kind} and {rest_money:.2f} leva left.")
else:
    needed_money = price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")