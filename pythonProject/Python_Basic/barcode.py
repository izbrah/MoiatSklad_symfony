from barcode import EAN13

number = '1234567890000'
ean_code = EAN13(number)
ean_code.save('Barcode')
