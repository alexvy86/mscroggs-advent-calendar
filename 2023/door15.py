import math


def calculate_arithmetic_mean(digits):
  return sum(digits) / len(digits)


def calculate_geometric_mean(digits):
  product = 1
  for digit in digits:
    product *= digit
  return math.pow(product, 1 / len(digits))


def find_smallest_number():
  for i in range(400, 500):
    digits = [int(d) for d in str(i)]
    arithmetic_mean = calculate_arithmetic_mean(digits)
    geometric_mean = calculate_geometric_mean(digits)
    if arithmetic_mean != 0 and arithmetic_mean % 1 < 0.0000000001:
      print(i, arithmetic_mean, geometric_mean)
      if geometric_mean != 0 and (geometric_mean % 1 < 0.0000000001 or geometric_mean % 1 > 0.99999999):
        return i


smallest_number = find_smallest_number()
print(smallest_number)
