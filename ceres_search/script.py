import re
f = open("ceres.txt","r")
f_lines = [line.split() for line in f]
count,newcount = 0,0
for line in f_lines:
    arr = re.findall(r"(?=(XMAS|SAMX))", line[0])
    count += len(arr)

rows = [row[0] for row in f_lines]
max_length = max(len(row) for row in rows)
transposed = [''.join(row[i] for row in rows) for i in range(max_length)]
transposed_matrix = [[col] for col in transposed]
for line in transposed_matrix:
    arr = re.findall(r"(?=(XMAS|SAMX))", line[0])
    count += len(arr)

for i in range(len(f_lines)-3):
    for j in range(len(f_lines[0][0])-3):
        pattern = f_lines[i][0][j] + f_lines[i+1][0][j+1] + f_lines[i+2][0][j+2] + f_lines[i+3][0][j+3]
        if pattern == "XMAS" or pattern == "SAMX":
            count += 1

for i in range(len(f_lines)-3):
    for j in range(3,len(f_lines[0][0])):
        pattern = f_lines[i][0][j] + f_lines[i+1][0][j-1] + f_lines[i+2][0][j-2] + f_lines[i+3][0][j-3]
        if pattern == "XMAS" or pattern == "SAMX":
            count += 1
print("Part 1 :",count)

for i in range(len(f_lines)-2):
    for j in range(len(f_lines[0][0])-2):
        pattern1 = f_lines[i][0][j] + f_lines[i+1][0][j+1] + f_lines[i+2][0][j+2]
        pattern2 = f_lines[i][0][j+2] + f_lines[i+1][0][j+1] + f_lines[i+2][0][j]
        if pattern1 in ["MAS","SAM"] and pattern2 in ["MAS","SAM"]:
            newcount += 1
print("Part 2 :",newcount)