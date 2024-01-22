int_number = int(input())
bonus = 0

if int_number <= 100:
    bonus =bonus+5
elif 100 < int_number <= 1000:
    bonus = int_number*0.2
elif int_number>1000:
    bonus = int_number*0.1


if int_number%2 == 0:
    bonus += 1
elif int_number%10 == 5:
    bonus += 2

print(bonus)
print(bonus+int_number)
