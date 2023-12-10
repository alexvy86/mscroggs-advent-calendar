import functools
current = 15
digit_sum = 6
while digit_sum != 15:
  print(f"{current} -> {digit_sum}")
  current += 15
  digit_sum = functools.reduce(
      lambda c, acc: acc + c, [int(x) for x in str(current)])
print(f"{current} -> {digit_sum}")
