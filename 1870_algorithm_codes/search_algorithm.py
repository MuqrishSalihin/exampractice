#sequential search 

def seqential_search(arr,key):
    i = 0
    while i < len(arr) and arr[i] != key:
        i = i+1
        
    if i < len(arr):
        return i  # returns the index of the key
    else:
        return -1
    

#binary search -> works only on sorted array

def binary_search(arr, key):
    left = 0
    right = len(arr)-1

    while left <= right:
        middle = (left + right) //2

        if key == arr[middle]:
            return middle
        elif key < arr[middle]:
            right = middle -1 #changing the new array upper bound
        else:
            left = middle + 1 #changing the new array lower bound

    return -1


array = [1,2,3,4,5,7,45,68,73,82]
K = 82
print(seqential_search(array,K))
print(f"{K} is located at {binary_search(array,K)}th index")