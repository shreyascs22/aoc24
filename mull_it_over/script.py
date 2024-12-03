import re
f = open("mull.txt","r")
str = f.read()
enabled = True
res,enabled_res = 0,0
result = []
mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
arr = re.findall(mul_pattern, str)
res += sum(int(pair[0])*int(pair[1]) for pair in arr)
print("Part 1 :",res)

matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", str)
for instruction in matches:
    if re.fullmatch(mul_pattern, instruction):
        if enabled:
            a, b = map(int, re.findall(r"\d+", instruction))
            result.append((a,b))
    elif re.fullmatch(do_pattern,instruction):
        enabled = True
    elif re.fullmatch(dont_pattern, instruction):
        enabled = False
    else:
        continue
enabled_res += sum(int(pair[0])*int(pair[1]) for pair in result)
print("Part 2 :",enabled_res)