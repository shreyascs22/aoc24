f = open("historian.txt", "r")
f_lines = [line.split() for line in f]
left, right = [],[]
res,total = 0,0
for i in range(len(f_lines)):
    left.append(int(f_lines[i][0]))
    right.append(int(f_lines[i][1]))

res += sum(left[i] * right.count(left[i]) for i in range(len(left)))
print("Part 2 : ",res)

left.sort()
right.sort()
total += sum(abs(left[i] - right[i]) for i in range(len(left)))
print("Part 1 : ", total)