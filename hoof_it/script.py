f = open("hoof.txt", "r")
f_lines = [list(line.strip()) for line in f]
trailheads, count, ncount, res = [], 0, 0, 0

def path(pos, visited, reachable_nines):
    global ncount
    if f_lines[pos[0]][pos[1]] == '9':
        reachable_nines.add((pos[0], pos[1]))
        ncount += 1
        return

    visited.add((pos[0], pos[1]))

    left, right, up, down = True, True, True, True
    if pos[0] == 0:
        up = False
    if pos[0] == len(f_lines) - 1:
        down = False
    if pos[1] == 0:
        left = False
    if pos[1] == len(f_lines[pos[0]]) - 1:
        right = False

    if left and (pos[0], pos[1] - 1) not in visited:
        if int(f_lines[pos[0]][pos[1] - 1]) - int(f_lines[pos[0]][pos[1]]) == 1:
            path([pos[0], pos[1] - 1], visited, reachable_nines)

    if right and (pos[0], pos[1] + 1) not in visited:
        if int(f_lines[pos[0]][pos[1] + 1]) - int(f_lines[pos[0]][pos[1]]) == 1:
            path([pos[0], pos[1] + 1], visited, reachable_nines)

    if up and (pos[0] - 1, pos[1]) not in visited:
        if int(f_lines[pos[0] - 1][pos[1]]) - int(f_lines[pos[0]][pos[1]]) == 1:
            path([pos[0] - 1, pos[1]], visited, reachable_nines)

    if down and (pos[0] + 1, pos[1]) not in visited:
        if int(f_lines[pos[0] + 1][pos[1]]) - int(f_lines[pos[0]][pos[1]]) == 1:
            path([pos[0] + 1, pos[1]], visited, reachable_nines)

    visited.remove((pos[0], pos[1]))

for i in range(len(f_lines)):
    for j in range(len(f_lines[i])):
        if f_lines[i][j] == '0':
            trailheads.append([i, j])

for trailhead in trailheads:
    visited = set()
    reachable_nines = set()
    ncount = 0
    path(trailhead, visited, reachable_nines)
    count += len(reachable_nines)
    res += ncount
print("Part 1 : ", count)
print("Part 2 : ",res)
