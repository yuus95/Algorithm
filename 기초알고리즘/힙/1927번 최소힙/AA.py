from sys import stdin
import heapq

heap = []


n = int(stdin.readline())

for _ in range(n):
    num = int(stdin.readline())

    if num == 0 :
        if len(heap) == 0 :
            print(0)
        else:
            print(heapq.heappop(heap))
    else :
        heapq.heappush(heap,num)


