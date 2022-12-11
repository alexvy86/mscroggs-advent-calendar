factors = [2, 3, 4, 5, 6, 7, 8]
current_multiples = [2, 3, 4, 5, 6, 7, 8]

current_min = min(current_multiples)

while any(x != current_min for x in current_multiples):
  min_index = current_multiples.index(current_min)
  current_multiples[min_index] += factors[min_index]
  current_min = min(current_multiples)

print(current_min)
