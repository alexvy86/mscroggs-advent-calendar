# How many integers are there between 100 and 1000 whose digits add up to an even number?
count = 0
for num in range(100, 1000):
  digit_sum = sum(int(digit) for digit in str(num))
  if digit_sum % 2 == 0:
    count += 1
print(count)
