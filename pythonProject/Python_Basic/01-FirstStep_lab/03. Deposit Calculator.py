deposit = float(input())
period = int(input())
interest = float(input())/100
sum = deposit + period * ((deposit * interest ) / 12)
print(sum)