f = open("disk.txt","r")
f_output = f.read()
seq, nseq, counter, ncounter, res, nres = [], [], 0, 0, 0, 0
for i in range(len(f_output)):
    if i%2 == 0:
        for j in range(int(f_output[i])):
            seq.append(counter)
        counter += 1
    else:
        for j in range(int(f_output[i])):
            seq.append('.')

char_positions = []
for i in range(len(seq)):
    if seq[i] != '.':
        char_positions.append(i)

j = len(char_positions) - 1
for i in range(len(seq)):
    if seq[i] == '.':
        seq[i], seq[char_positions[j]] = seq[char_positions[j]], seq[i]
        j -= 1
    if i >= char_positions[j]:
        break

for i in range(len(seq)):
    if seq[i] == '.':
        break
    res += i*seq[i]
print("Part 1 : ",res)

for i in range(len(f_output)):
    if i%2 == 0:
        nseq.append(str(ncounter) * int(f_output[i]))
        ncounter += 1
    else:
        nseq.append('.' * int(f_output[i]))

nchar_positions = []
for i in range(len(nseq)):
    if nseq[i] != '.':
        nchar_positions.append(i)

for i in range(len(nchar_positions) - 1,-1,-1):
    print(i)
    for j in range(nchar_positions[i]):
        if nseq[j] and nseq[j][0] == '.':
            if len(nseq[nchar_positions[i]]) == len(nseq[j]):
                nseq[j], nseq[nchar_positions[i]] = nseq[nchar_positions[i]], nseq[j]
print(nseq)