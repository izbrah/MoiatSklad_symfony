import math

name_serial = input()
serial_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration * 1/8
rest_ruration = break_duration * 1/4
needed_time = lunch_duration + rest_ruration + serial_duration

if break_duration >= needed_time:
    extended_time = break_duration - needed_time
    print(f"You have enough time to watch {name_serial} and left with {math.ceil(extended_time)} minutes free time.")
else:
    extended_time = needed_time -  break_duration
    print(f"You don't have enough time to watch {name_serial}, you need {math.ceil(extended_time)} more minutes.")

