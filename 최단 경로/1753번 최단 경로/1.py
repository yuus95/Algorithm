import heapq
import sys
sys.stdin=open("00.txt")

def dijkstra(graph,start):
    distance = [2147000000] * (V+1)
    distance[start] = 0
    q=[]
    heapq.heappush(q,(0,start))


    while q:
        dist,destination = heapq.heappop(q)
        if distance[destination] < dist :
            continue
        for v,d in graph[destination]:
            next_value = dist + v
            if distance[d] > next_value:
                distance[d] = next_value
                heapq.heappush(q,(next_value,d))

    return distance




V,E = map(int,input().split())

start = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))


dist = dijkstra(graph,start)

for i in range(len(dist)):
    if i == 0 :
        continue
    if dist[i] == 2147000000:
        print("INF")
    else:
        print(dist[i])