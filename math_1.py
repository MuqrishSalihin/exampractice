arr = [1,2,3,4,6,7,9,8,10,-4,100,56,27,39,50,-89]
min_list = []
max_list = []


for i in range(0,len(arr)-1,2):
    if arr[i]> arr[i+1]:
        max_list.append(arr[i])
        min_list.append(arr[i+1])
    if arr[i+1] > arr[i]:
        max_list.append(arr[i+1])
        min_list.append(arr[i])

    max_val = max_list[0]
    min_val = min_list[0]

#finding the maximum value

for i in range(1, len(max_list)):
    if max_list[i] > max_val:
        max_val = max_list[i]

for i in range(1, len(min_list)):
    if min_list[i] < min_val:
        min_val = min_list[i]

print(min_list)
print(max_list)

print(f"The maximum value of the array is: {max_val}")
print(f"The minimum value of the array is: {min_val}")

    



