def search(lst, target):
    left, right = 0, len(lst) - 1
    
    while(left <= right):

        mid = left + (right - left) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(search([1,2,3,4,5,6,7,8,9,10], 8))