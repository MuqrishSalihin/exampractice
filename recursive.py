def h(n,k):
    if k == 1:
        return n
    else:
        if n == k :
            return 1
        else: 
            return h(n-1,k-1) + h(n-1,k)

print(f"The value of function h is {h(5,3)}")