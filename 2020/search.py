def linear_search(data,value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1

data = [1,2,3,4,5,6,7,8,9,10]
print(linear_search(data,5))
