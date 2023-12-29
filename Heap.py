import heapq
# Max Heap
maxHeap = []

heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# Min Heap
minHeap = []

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

while len(minHeap):
    print(heapq.heappop(minHeap))

# Heapify a list
nums = [1, 3, 2, 5, 4]
heapq.heapify(nums)

while nums:
    print(heapq.heappop(nums))