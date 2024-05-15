def sorted_square(array):
    n = len(array)
    res = [0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        res[i] = array[i]**2
    res.sort()
    return res

array = [-2,-5,-7,0,2,4,8]
print(sorted_square(array))