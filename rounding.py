print(round(1.5, 0))
print(round(2.5, 0))
print(round(10253, -2))
print(round(10253, 2))

print(0.1 + 0.2)

import decimal

target1 = 1.5
target2 = 2.5

rounded1 = decimal.Decimal(target1).quantize(decimal.Decimal('0.'), rounding=decimal.ROUND_HALF_UP)
print(rounded1)
rounded2 = decimal.Decimal(target2).quantize(decimal.Decimal('0.'), rounding=decimal.ROUND_HALF_UP)
print(rounded2)

print(rounded1 + rounded2)
print((rounded1 * rounded2).quantize(decimal.Decimal('0.00')))

target3 = 0.1
rounded3 = decimal.Decimal(str(target3))
print(rounded3)
