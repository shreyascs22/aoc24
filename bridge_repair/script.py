f = open("bridge.txt")
f_lines = [line.split() for line in f]
left_side, right_side, res, res_concat = [], [], 0, 0

for entry in f_lines:
    left_side.append(int(entry[0].strip(':')))
    right_side.append(list(map(int, entry[1:])))

# Part 1: Evaluate using only '+' and '*' operators
for idx in range(len(right_side)):
    array = right_side[idx]
    target = left_side[idx]
    operators = ['+', '*']
    num_operators = len(array) - 1
    total_combinations = 2 ** num_operators
    found = False

    for combination in range(total_combinations):
        current_ops = []
        temp = combination
        for _ in range(num_operators):
            current_ops.append(operators[temp % 2])
            temp //= 2
        current_ops.reverse()
        result = array[0] 
        for j in range(num_operators):
            if current_ops[j] == '+':
                result += array[j + 1]
            elif current_ops[j] == '*':
                result *= array[j + 1]
        if result == target:
            res += target
            found = True
            break  
print("Part 1:", res)

# Part 2: Evaluate using '+', '*' and '||' operators (concatenation)
res_concat = 0
for idx in range(len(right_side)):
    array = right_side[idx]
    target = left_side[idx]
    operators = ['+', '*', '||']
    num_operators = len(array) - 1
    total_combinations = 3 ** num_operators
    found = False

    for combination in range(total_combinations):
        current_ops = []
        temp = combination
        for _ in range(num_operators):
            current_ops.append(operators[temp % 3])
            temp //= 3
        current_ops.reverse()
        result = array[0]
        for j in range(num_operators):
            if current_ops[j] == '+':
                result += array[j + 1]
            elif current_ops[j] == '*':
                result *= array[j + 1]
            elif current_ops[j] == '||':
                result = int(str(result) + str(array[j + 1]))

        if result == target:
            res_concat += target
            found = True
            break  
print("Part 2:", res_concat)
