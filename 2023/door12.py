# 1! = 1
# 2! = 1 2
# 3! = 1 2 3
# 4! = 1 2 3 4
# 5! = 1 2 3 4 5
# 6! = 1 2 3 4 5 6
# 7! = 1 2 3 4 5 6 7
# 8! = 1 2 3 4 5 6 7 8

# In the final product:
# - Odds show up an even number of times, so each one shows up as multiplied by itself
# some number of times, which is a square number.
# - Evens show up an odd number of times, so each one shows up as multiplied by itself
# some number of times, plus one additional time.
#
# When we divide by some n!, we're removing one row from the pyramid above.
# Whatever number we choose, we're swapping the number of times that each number less than or equal to
# n shows up.
# If we choose an even N, the odd numbers less than N and the even numbers greater than N (up to the target)
# end up showing up multiplied by themselves an odd number of times, so we need to ensure that multiplying
# all of them is a square number.
# If we choose an odd N, the odd numbers less than or equal to N and the even numbers greater than N (up to
# the target) end up showing up multiplied by themselves an odd number of times, so we need to ensure that
# multiplying all of them is a square number.

from math import prod


def is_square_number(number):
  sqrt = pow(number, 0.5)
  return sqrt % 1 < 0.00000001 or sqrt % 1 > 0.99999999


for n in range(100, 501):
  min_even = n + 2 if n % 2 == 0 else n + 1
  odds_without_squares = [x for x in range(1, n, 2) if not is_square_number(x)]
  evens_without_squares = [x for x in range(
      min_even, 501, 2) if not is_square_number(x)]

  # Simplify the even numbers by dividing by 2 as much as possible. We want to make the total number of divisions even,
  # which means that we removed multiplications by 4 which are square numbers.
  processed_evens = []
  how_many_times_divided_by_2 = 0
  for x in evens_without_squares:
    current = x
    while current % 2 == 0:
      current /= 2
      how_many_times_divided_by_2 += 1
    processed_evens.append(current)
  if how_many_times_divided_by_2 % 2 == 1:
    processed_evens.append(2)

  # Numbers that exist in both lists can be removed because they're going to multiply into a square number
  index = 0
  while index < len(odds_without_squares):
    x = odds_without_squares[index]
    if x in processed_evens:
      odds_without_squares.remove(x)
      processed_evens.remove(x)
    else:
      x += 1

  # Repeated numbers in each list can be removed because they're going to multiply into a square number
  index = 0
  while index < len(processed_evens):
    x = processed_evens[index]
    if processed_evens.count(x) > 1:
      while processed_evens.count(x) > 1:
        processed_evens.remove(x)
        processed_evens.remove(x)
    else:
      index += 1

  # Simplify the even numbers again by removing squares that might have showed up
  processed_evens = [x for x in processed_evens if not is_square_number(x)]

  prod_of_odds = prod(odds_without_squares)
  prod_of_evens = prod(processed_evens)
  unknown = prod_of_odds * prod_of_evens
  print(f"n: {n}\nows: {sorted(odds_without_squares)}\np_o: {prod_of_odds}\news: {sorted(processed_evens)}\np_e:{prod_of_evens}\nu: {unknown}")
  square_root = pow(unknown, 0.5)
  print(f"sqrt: {square_root}")
  if square_root % 1 < 0.00000001 or square_root % 1 > 0.99999999:
    break
