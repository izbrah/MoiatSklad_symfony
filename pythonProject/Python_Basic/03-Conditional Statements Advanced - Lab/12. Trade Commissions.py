city = input()
sells = float(input())

error_condition = False
commision = 0;
if city == "Sofia":
    if 0 <= sells <= 500:
      commision = 5/100 * sells
    elif 500 < sells <= 1000:
        commision = 7 / 100 * sells
    elif 1000 < sells <= 10000:
        commision = 8 / 100 * sells
    elif 10000 < sells:
        commision = 12 / 100 * sells
    else:
        error_condition = True
elif city == "Varna":
    if 0 <= sells <= 500:
        commision = 4.5 / 100 * sells
    elif 500 < sells <= 1000:
        commision = 7.5 / 100 * sells
    elif 1000 < sells <= 10000:
        commision = 10 / 100 * sells
    elif 10000 < sells:
        commision = 13 / 100 * sells
    else:
        error_condition = True
elif city == "Plovdiv":
    if 0 <= sells <= 500:
        commision = 5.5 / 100 * sells
    elif 500 < sells <= 1000:
        commision = 8 / 100 * sells
    elif 1000 < sells <= 10000:
        commision = 12 / 100 * sells
    elif 10000 < sells:
        commision = 14.5 / 100 * sells
    else:
        error_condition = True
else:
    error_condition = True

if error_condition:
    print("error")
else:
    print( f"{commision:.2f}")
