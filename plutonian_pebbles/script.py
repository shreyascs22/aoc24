def blinks(arr):
    for counter in range(75):
        print(counter,"/",75)
        new_arr = []
        for i in range(len(arr)):
            if arr[i] == 0:
                new_arr.append(1)
            elif len(str(arr[i])) % 2 == 0:
                ele = str(arr[i])
                left = ele[:len(ele)//2]
                right = ele[len(ele)//2:]
                new_arr.append(int(left))
                new_arr.append(int(right))
            else:
                new_arr.append(arr[i] * 2024)
        arr = new_arr
    return arr

source_arr = [4022724,951333,0,21633,5857,97,702,6]
#source_arr = [125,17]
res_arr = blinks(source_arr)
print(f"Final arrangement: {res_arr}")
print(f"Length of final array: {len(res_arr)}")
