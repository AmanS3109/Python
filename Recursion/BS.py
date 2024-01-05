def search(array, target, start, end):
    if start > end:
        return -1

    mid = start + (end - start) // 2

    if array[mid] == target:
        return mid

    if target < array[mid]:
        return search(array, target, start, mid - 1)

    return search(array, target, mid + 1, end)


array = [1, 3, 5, 55, 66, 96]
target = int(input("What is target: "))
answer = search(array, target, 0, len(array) - 1)
print(answer)
