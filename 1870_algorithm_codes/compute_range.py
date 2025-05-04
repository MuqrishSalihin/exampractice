


def Mystery1(): 
    arr = [5,3,7,6,1]
    x = arr[0]
    y = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > x:
            x = arr[i]
        elif arr[i] < y:
            y = arr[i]

    return x-y


def Mystery2():
    arr = [2,4,7,3]
    n = (len(arr)/2) -1
    for i in range(0,int(n)):
        tmp = arr[i]
        arr[i] = arr[int(n)-i-1]
        arr[int(n)-i-1] = tmp
    
    return arr

print(Mystery2())

def longest_consecutive(arr):

    consecutive_counter = 0
    temp = arr[0]
    sorted_arr = []

    # sort the array increasingly

    for i in range(1, len(arr)):

        





arr = [1,2,3,100,200,4]