def search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


list0 = [-7, 5, 9, 22, 69, 99]   #sorted list
target = int(input("Enter the number you want to search: "))
ans = search(list0, target)
print("The number is present at index: ", ans)