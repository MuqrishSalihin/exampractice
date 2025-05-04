def h(n,k):
    if k == 1:
        return n
    else:
        if n == k :
            return 1
        else: 
            return h(n-1,k-1) + h(n-1,k)

print(f"The value of function h is {h(5,3)}")


def factorial(n):
    if n == 0: 
        return 1
    else:
        return factorial(n-1)*n
    
    
n = int (input("Calculate factorial:"))  #exxplicit casting
print(factorial(n))


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

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middle = len(arr) //2 
    left_arr = arr[:middle]
    right_arr = arr[middle:]

    sorted_left = merge_sort(left_arr)
    sorted_right = merge_sort(right_arr)

    return merge(sorted_left, sorted_right)
    
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

print(f"The sorted array for {array} is {sorted_array}")






    
