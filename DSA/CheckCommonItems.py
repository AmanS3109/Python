arr1 = ['a', 'b', 'c', 'x']
arr2 = ['z', 'y', 'r']


def contains_common_item(array1, array2):
    # Loop through arr1 and create a set where each element is a key in the set
    items_set = set()
    for item in array1:
        items_set.add(item)

    # Loop through arr2 and check if any element is in the set
    for item in array2:
        if item in items_set:
            return True

    return False


print(contains_common_item(arr1, arr2))
