'''
nums = [2, 7, 11, 15]
target = 9
output -> 
'''

lst = [3, 5, 5, 4]
target = 10

def twoSum(lst):
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return i, j
            

print(twoSum(lst))


'''Basic and straight forward approach'''