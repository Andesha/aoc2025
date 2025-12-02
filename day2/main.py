import sys

with open(sys.argv[1]) as f:
    content = [map(int, item.split('-')) for item in f.read().split(',')]

p1_invalids, p2_invalids = set(), set()
for left, right in content:
    for i in range(left, right+1):
        treat_str = str(i)
        
        length = len(treat_str)
        if length % 2 == 0 and (treat_str[:length//2] == treat_str[length//2:]):
            p1_invalids.add(i)
        
        for j in range(1, length//2 + 1):
            if length % j == 0 and (treat_str == treat_str[:j] * (length // j)):
                p2_invalids.add(i)

print('Part 1: ', sum(p1_invalids))
print('Part 1: ', sum(p2_invalids))