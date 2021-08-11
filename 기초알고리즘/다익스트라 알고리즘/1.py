import collections
import heapq
import sys
input = sys.stdin.readline

V,E = map(int,input().split())

graph = []


# 방향 그래프
for _ in range(V):
    u,v,w = map(int,input().split())
    graph[u].append(v,w)


def dijkstra(graph,start):
    q = [(0,start)]
    distance = collections.defaultdict(int)

    while q:
        dist, node = heapq.heappop(q)
        if node not in distance:
            distance[node] = dist
            for v,w in graph[node]:
                update = dist+ w
                heapq.heappush(0,(Q,(update,v)))

    if len(dist) == V:
        return max(distance.values())
    return -1
