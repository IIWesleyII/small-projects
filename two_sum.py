# Two Sum
# determine if there are two numbers in a list that adds to a target value

# loop through lst
#  init first val
# init curr vall
# if curr val + first val == target : return True
# end loops
# return False

# O(n^2)

def two_sum(lst , n):
    for i in range(0 ,len(lst)):
        for j in range(0,len(lst)):
            if i == j:
                pass
            elif lst[i] + lst[j] == n:
                return True
    return False

#print(f'7 {two_sum([1,2,4,5,3,2,7,8,12,19,20], 7)}')
#print(f'33 {two_sum([1,2,4,5,20], 33) }')
#print(f'0 {two_sum([], 0) }')
#print(f'1 {two_sum([1], 1) }')

# set solution for O(n)

#loop through every element 
# put val = element - n in set , if val in list return true
# return false after loop completes 
def sums(lst, n):
    s = set()
    for x in lst:
        if x in s:
            return True
        s.add(n-x)
    return False

print(f'8 {sums([1,2,3,4,2] , 8)}')