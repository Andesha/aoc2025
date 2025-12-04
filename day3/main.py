import sys
from collections import Counter

with open(sys.argv[1]) as f:
    content = [list(map(int, str(item))) for item in f.read().splitlines()]

accum = 0
for row in content:
    max_val, length = -1, len(row)
    for i in range(length):
        for j in range(i + 1, length):
            max_val = max(max_val, (10 * row[i]) + row[j])
    accum += max_val
print('Part 1:', accum)

# Only works for small test problem:
# all_combinations = set(combinations(range(len(content[0])), 12))
# accum = 0
# for row in content:
#     max_val, length = -1, len(row)
#     for combo in all_combinations:
#         max_val = max(max_val, int(''.join(str(row[index]) for index in combo)))
#     accum += max_val
# print('Part 2: ', accum)

accum, batteries = 0, 12
for row in content:
    max_voltage, buffer = 0, 0
    for offset in range(batteries, 0, -1):
        window = row[buffer:len(row) - offset + 1]
        max_d = max(digit for digit in window)
        buffer += window.index(max_d) + 1
        max_voltage = 10 * max_voltage + max_d
    accum += max_voltage
print('Part 2:', accum)