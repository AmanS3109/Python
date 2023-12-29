nums = [1, 2, 3]

# using index
for i in range(len(nums)):
    print(i)

# without using index
for num in nums:
    print(num)

# using enumerate
for i, num in enumerate(nums):
    print(i, num)

# loop through multiple lists
names = ['aman', 'shruti', 'shaikada']
ages = [21, 20, 19]
for n1, n2 in zip(names, ages):
    print(n1, n2)

# loop in reverse
for num in reversed(nums):
    print(num)

# or using reverse method
nums.reverse()
print(nums)

# loop in sorted order
nums2 = [1, 3, 2, 5, 4]
nums2.sort()
print(nums2)
nums2.sort(reverse=True)  # for descending order
print(nums2)

# list comprehension
# [expression for item in list]
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)

# list comprehension with if statement
# [expression for item in list if condition]
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
print(even_squares)

# 2D list
nums3 = [[0]*4 for _ in range(4)]
print(nums3)

