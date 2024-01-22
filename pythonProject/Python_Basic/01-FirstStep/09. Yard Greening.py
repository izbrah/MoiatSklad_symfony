yard = float(input())
yard_price = yard * 7.61
discout = yard_price * 0.18
yard_price = yard_price - discout
print(f"The final price is: {yard_price} lv.")
print(f"The discount is: {discout} lv.")