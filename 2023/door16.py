def smallest_three_digit_number():
  for n in range(100, 1000):
    for i in range(1, n):
      consecutive_numbers = []
      min_consecutive = i
      for j in range(i, n):
        consecutive_numbers.append(j)
        sum_of_consecutive = sum(consecutive_numbers)
        if sum_of_consecutive == n:
          print(n, consecutive_numbers)
          break
        elif sum_of_consecutive > n:
          consecutive_numbers.pop(0)
          sum_of_consecutive = sum(consecutive_numbers)
          min_consecutive += 1
          if sum_of_consecutive == n:
            print(n, consecutive_numbers)
            break
      if sum_of_consecutive == n:
        print(n, consecutive_numbers)
        break
    if sum_of_consecutive != n:
      return n


smallest_number = smallest_three_digit_number()
print(smallest_number)
