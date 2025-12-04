import sys

with open(sys.argv[1]) as f:
    maze = [list(item) for item in f.read().splitlines()]
depth, width = len(maze), len(maze[0])

accum = 0
while True:
    valid = set()
    for y in range(depth):
        for x in range(width):
            if maze[y][x] == '@':
                rolls_beside = -1
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= (x+i) < width and 0 <= (y+j) < depth:
                            if maze[y+j][x+i] == '@':
                                rolls_beside += 1
                if rolls_beside < 4:
                    valid.add((y, x))

    for y,x in valid:
        maze[y][x] = '.'

    accum += len(valid)
    if not valid:
        break

    print('Part 1:', len(valid))
print('Part 2:', accum)