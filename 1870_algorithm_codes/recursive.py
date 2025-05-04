

def h(n,k):
    if k == 1:
        return n
    else:
        if n == k :
            return 1
        else: 
            return h(n-1,k-1) + h(n-1,k)

print(f"The value of function h is {h(5,3)}")


#factorial recursion 

def factorial(n):
    if n == 0: 
        return 1
    else:
        return factorial(n-1)*n
    
    
n = int (input("Calculate factorial:"))  #explicit casting
print(factorial(n))

#binary search recursion 
#time complexity = O(log n)

def binary_search(arr,K, left = 0, right = None):
    if right == None:
        right = len(arr) -1

    middle = (left + right) //2

    if K == arr[middle]:
        return middle
    elif K < arr[middle]:
        return binary_search(arr, K,left = 0, right = middle -1)
    elif K > arr[middle]:
        return binary_search(arr, K, left = middle +1, right = None)
    

array = [1,2,3,4,5,7,45,68,73,82]
K = 82
print(f"{K} is located at {binary_search(array,K)}th index")

#Merge sort algorithm
# Time complexity = O(nlog n)

def merge_sort(arr):

    if len(arr) <= 1:
        return arr  #this is the base case

    middle = len(arr) //2 
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    #all the code above, is basically slicing the array, until each element of the array formed =1
    return merge(merge_sort(left_arr), merge_sort(right_arr))
    
def merge(left,right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

array = [7,2,9,4,3,1,5,8]
sorted_array = merge_sort(array)

for elements in sorted_array:
    print(elements)

print(f"The sorted array for {array} is {sorted_array}")


#quick sort algorithm 
#the key keeps moving, according to the array.

def partition (arr, low, high):
    pivot  = arr[high]

    i = low - 1   #index = -1

    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i ,j)
    swap(arr, i + 1, high)
    return i + 1

def swap (arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 

def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)

        #this is where the sorting begins
        quick_sort(arr, low, partition_index - 1) #sorting below pivot
        quick_sort(arr, partition_index + 1, high) #sorting above pivot

array = [7,2,9,4,3,1,5,8]
n = len(array)

quick_sort(array, 0, n-1)

print(array)




    
