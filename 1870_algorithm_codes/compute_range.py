


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



def sorting(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while (j >= 0 and arr[j] > temp):
            arr[j+1] = arr[j] #switch happens
            j-=1
        arr[j+1] = temp
    return arr

def consecutive_num(s_a):
    maximum = 1
    current = 1

    for i in range(len(s_a)-1):
        if s_a[i+1] - s_a[i] == 1: 
            current+=1
            maximum = max(current, maximum)
        else:
            current = 1
    
    return maximum

array = [3,1,2,100,200,4,201,202,203,204,205,206]
sortedArray = sorting(array)
n = consecutive_num(sortedArray)
print(sortedArray)
print(n)