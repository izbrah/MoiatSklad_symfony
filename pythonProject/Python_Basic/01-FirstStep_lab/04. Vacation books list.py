sheets = int(input())
readed_sheets_per_hour = int(input())
days = int(input())
hours = sheets / readed_sheets_per_hour
hours_per_day = int(hours // days)
print(hours_per_day)
