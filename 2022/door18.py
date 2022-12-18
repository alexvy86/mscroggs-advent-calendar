'''
 3	 5	 2	10	10
 1	 4	 7	12	12
 6	 8	 9	23	23
10	12	23
10	12	23

3 * 2 * 4 * 6 = 144

Deduced that b_x(14) != 4.
Combinations of b_x0 and speed_x with that result cannot be true. Which are those?
'''

import itertools

initial_x = [2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
speed_x   = [1, 2, 4, 5, 7, 8, 10, 12, 14, 15, 17, 18, 19, 20]

discarded_combinations = []
print("Discard")
for (x0, speed) in itertools.product(initial_x, speed_x):
	# Discard based on blue_x(14) != 4
	if (x0 + 13*speed) % 20 == 4:
		# print(f"({x0} - {speed})")
		discarded_combinations.append((x0,speed))

	# Discard based on the coords tried on 12/17
	if ((x0 + 16*speed) % 20, (9 + 16*15) % 20) in [(1,9),(2,9),(3,9),(9,9)]:
		# print(f"({x0} - {speed})")
		discarded_combinations.append((x0,speed))

	# Discard based on blue_x(15) = 5
	if (x0 + 14*speed) % 20 != 5:
		# print(f"({x0} - {speed})")
		discarded_combinations.append((x0,speed))


print("Candidates for 12/18")
candidates = []
for (x0, speed) in itertools.product(initial_x, speed_x):
	if (x0, speed) not in discarded_combinations:
		candidates.append(f"({(x0 + 17*speed) % 20}, {(9 + 17*15) % 20}) (x0={x0}, speed_x={speed})")
candidates.sort()
for c in candidates:
	print(c)
