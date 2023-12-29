def linearSearch(array, target):
    if len(array) == 0:
        return -1
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


array = [34, 23, 5, 7 , 1, -9, -4, 23]
target = int(input("Enter the number you want to search: "))
ans = linearSearch(array, target)
print("The number is present at index: ", ans)

