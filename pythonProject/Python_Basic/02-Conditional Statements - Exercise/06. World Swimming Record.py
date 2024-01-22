# 1. Рекордът в секунди – реално число;
import math

swimming_record =float(input())
# 2. Разстоянието в метри – реално число;
distance = float(input())
# 3. Времето в секунди, за което плува разстояние от 1 м. - реално число.
time_swimming_per_meter = float(input())

resistance_delay = math.floor((distance / 15)) * 12.5
time_swimming = time_swimming_per_meter * distance + resistance_delay

if time_swimming < swimming_record:
    print(f" Yes, he succeeded! The new world record is {time_swimming:.2f} seconds.")
else:
    shortage = time_swimming - swimming_record
    print(f"No, he failed! He was {shortage:.2f} seconds slower.")
