def linear_search(data,value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1

def binary_search(data,value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

data = [1,2,3,4,5,6,7,8,9,10,35,36,37,40,80,90]
print(linear_search(data,40))
print(binary_search(data,90))