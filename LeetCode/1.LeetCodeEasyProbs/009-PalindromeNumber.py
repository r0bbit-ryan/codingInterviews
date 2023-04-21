var = 10001

def palindromeNum(x):
    # My solution - not optimal
    '''lst = [str(i) for i in x]
    templst = []
    temp = ""

    if x[0] != x[-1]:
        return False

    for i in range(0, len(lst)):
        for j in range(i, len(lst)):
                temp = temp + lst[j]
        if len(temp) == len(x):
            templst.append(temp)
        temp = ""

    for t in templst:
        if t == t[::-1]:
            return True

    return False'''

    #Best solution
    x = str(x)
    return x == x[::-1]


print(palindromeNum(var))
    