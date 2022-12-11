# candidates = range(100,1000)
candidates = range(0,11111112)

how_many = 0
for c in candidates:
  c_str = str(c)
  if c_str.find("0") >= 0 or c_str.find("9") >= 0:
    continue
  if c_str.find("8") >= 0 and len(c_str) > 1:
    continue
  if sum(int(digit) for digit in str(c)) == 8:
    how_many += 1

print(how_many)
