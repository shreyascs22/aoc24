f = open("reports.txt", "r")
f_lines = [list(map(int, line.split())) for line in f]
count, newcount = 0, 0

def levels(arr):
    for j in range(1, len(arr) - 1):
        if arr[j] > arr[j - 1] and arr[j] > arr[j + 1]:
            return 0
        if arr[j] < arr[j - 1] and arr[j] < arr[j + 1]:
            return 0
        if abs(arr[j] - arr[j - 1]) < 1 or abs(arr[j] - arr[j + 1]) > 3:
            return 0
        if abs(arr[j] - arr[j - 1]) > 3 or abs(arr[j] - arr[j + 1]) < 1:
            return 0
    return 1

for line in f_lines:
    safe_arr = levels(line)
    if safe_arr: 
        count += 1
        newcount += 1
    else:
        for i in range(len(line)):
            line_copy = line[:]
            del line_copy[i]
            rechk_safe_arr = levels(line_copy)
            if rechk_safe_arr:
                newcount += 1
                break

print("Part 1:", count)
print("Part 2:", newcount)
