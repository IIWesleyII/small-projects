def binary_search(lst, target):
    left, right = 0 , len(lst) - 1

    while left <= right:
        mid = left + (right - 1) // 2;
        # Check if x is present at mid
        if lst[mid] == target:
            return mid
        # If x is greater, ignore left half
        elif lst[mid] < target:
            left = mid + 1
        # If x is smaller, ignore right half
        else:
            right = mid - 1  
    return -1
target = 10 
#print(binary_search([ 2, 3, 4, 10, 40 ],  target))

lst = [2,3,4,5,6,7,8]
target = 3
print(lst.index(3))
