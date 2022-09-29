import heapq

ls = [2,3,4,5,4,3,2,4,5,6]

heapq.heapify(ls)

print(heapq.heappop(ls))

import heapq

heapq.heapify(ls)
heapq.heappush(ls, 30)
print(ls)