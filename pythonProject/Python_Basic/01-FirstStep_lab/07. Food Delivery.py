chick = int(input())
fish = int(input())
veg = int(input())

chick = chick*10.35
fish = fish*12.4
veg = veg*8.15
delivery = 2.5

sum = chick+fish+veg
desert = sum*0.2
sum = sum+desert+delivery
print(sum)
