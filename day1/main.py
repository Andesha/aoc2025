import sys

with open(sys.argv[1]) as f:
    content = [(item[0], int(item[1:])) for item in f.read().splitlines()]

position = 50
click_count, count = 0, 0
for direction, amount in content:
    if direction == 'L':
        position = (position - amount)
    else:
        position = (position + amount)
    
    if position > 99 or position < 0:
        click_count += abs(position//100)
    
    position = position % 100
    if position == 0:
        count += 1

print('Part 1: ', count)
print('Part 2: ', click_count)