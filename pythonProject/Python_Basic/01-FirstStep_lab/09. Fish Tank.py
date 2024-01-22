length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length*width*height
water = (volume -
         volume*percent/100)*0.001
print(water)

