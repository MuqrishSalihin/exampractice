#selection sort algorithm

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j #got the minimum value of the array
        #swap a[i] and a[mini]
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
    return arr


def bubble_sort(arr):
    for a in range(0, len(arr)-2): #how many times we go through the array
        for b in range(0, len(arr)-2-a): #how many times we switch for each array traversal
            if arr[b] > arr[b+1]:
                tmp = arr[b]
                arr[b] = arr[b+1]
                arr[b+1] = tmp
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1

        while (j>=0 and temp< arr[j]):
            arr[j+1] = arr[j] #switch
            j -=1
        arr[j+1] = temp
    return arr
            
            


array = [89,45,68,90,34,17]

print(selection_sort(array))
print(bubble_sort(array))
print(insertion_sort(array))