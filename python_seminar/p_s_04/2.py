import math
import decimal

d = 0.0001
precision = str(d)
precision = decimal.Decimal(precision)
precision = precision.as_tuple().exponent
precision = abs(precision)
print(precision)

number = round(math.pi, precision)
print(number)