tax_for_year = int(input())

snickers = tax_for_year - tax_for_year*0.4
equipment = snickers - snickers*0.2
ball = equipment/4
accessories = ball/5
price = tax_for_year  +snickers+equipment+ball+accessories
print(price)
# print(f'snickers:{snickers};equipment:{equipment};ball:{ball};accessories:{accessories}')