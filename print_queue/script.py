fpairs = open("pairs.txt","r")
fqueue = open("queue.txt","r")
lines = fqueue.read().split('\n')
queue = [list(map(int, line.split(','))) for line in lines]
pairs = fpairs.read().split('\n')
arr, bad_array, res, output = [],[],0,0

for i in range(len(queue)):
    flag = True
    for j in range(len(queue[i])-1):
        for k in range(j+1,len(queue[i])):
            string = str(queue[i][k]) + "|" + str(queue[i][j])
            if string in pairs:
                flag = False
                break
        if not flag:
            break
    if flag:
        arr.append(queue[i])

for line in arr:
    res += line[len(line)//2]
print("Part 1 :",res)

for line in queue:
    if line not in arr:
        bad_array.append(line)

for i in range(len(bad_array)):
    for j in range(len(bad_array[i])-1):
        for k in range(j+1,len(bad_array[i])):
            string = str(bad_array[i][k]) + "|" + str(bad_array[i][j])
            if string in pairs:
                bad_array[i][j], bad_array[i][k] = bad_array[i][k], bad_array[i][j]

for line in bad_array:
    output += line[len(line)//2]
print("Part 2 : ",output)