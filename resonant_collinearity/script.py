f = open("trial.txt")
lines = [line.split() for line in f]
f_lines = [line[0] for line in lines]
char_positions, row_index, path, npath = {}, 0, [], []
for row in f_lines:
    col_index = 0
    for char in row:
        if char != '.':
            if char not in char_positions:
                char_positions[char] = []
            char_positions[char].append((row_index, col_index))
        col_index += 1
    row_index += 1

for char, positions in char_positions.items():
    for i in range(len(positions)-1):
        for j in range(i+1,len(positions)):
            x1,y1,x2,y2 = positions[i][0], positions[i][1], positions[j][0],positions[j][1]
            x_diff,y_diff = x2-x1,y2-y1
            if x1-x_diff >= 0 and y1-y_diff >= 0 and x1-x_diff < len(f_lines) and y1-y_diff < len(f_lines[0]):
                if [x1-x_diff,y1-y_diff] not in path:
                    path.append([x1-x_diff,y1-y_diff])
                    while x1-x_diff >= 0 and y1-y_diff >= 0 and x1-x_diff < len(f_lines) and y1-y_diff < len(f_lines[0]):
                        if [x1-x_diff,y1-y_diff] not in npath:
                            npath.append([x1-x_diff,y1-y_diff])
                        x1,y1 = x1-x_diff,y1-y_diff

            if x2+x_diff < len(f_lines) and y2+y_diff < len(f_lines[0]) and x2+x_diff >= 0 and y2+y_diff >= 0:
                if [x2+x_diff,y2+y_diff] not in path:
                    path.append([x2+x_diff,y2+y_diff])
                    while x2+x_diff >= 0 and y2+y_diff >= 0 and x2+x_diff < len(f_lines) and y2+y_diff < len(f_lines[0]):
                        if [x2+x_diff,y2+y_diff] not in npath:
                            npath.append([x2+x_diff,y2+y_diff])
                        x2,y2 = x2+x_diff,y2+y_diff
print("Part 1 : ",len(path))
print("Part 2 : ",len(npath))