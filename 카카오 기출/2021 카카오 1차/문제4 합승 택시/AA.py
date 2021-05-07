#블로그 참조  https://chocochip101.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-%ED%95%A9%EC%8A%B9-%ED%83%9D%EC%8B%9C-%EC%9A%94%EA%B8%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%EB%B0%8F-%ED%92%80%EC%9D%B4
import heapq

def solution(n,s,a,b,fares):

    link =[[]for _ in range(n+1)]
    for x,y ,z in fares:
        link[x].append((z,y))
        link[y].append((z,x))


    def dijkstra(start):
        dist = [987654321] * (n+1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap,(0,start))

        while heap:
            value,destination = heapq.heappop(heap) #스타트와 거리가 가까운 순부터 계속 꺼내서 구함


            if dist[destination] < value:
                continue

            for v , d in link[destination]: #꺼내온 노드들의  간선 비용 이랑 최소비용 비교
                next_value = value + v
                if dist[d] > next_value:
                    dist[d]= next_value
                    heapq.heappush(heap,(next_value,d))
            print(dist)

        return dist


    dp =[[]] + [dijkstra(i) for i in range(1,n+1)]
    answer = 987654321
    for i in range(1,n+1):
        answer = min(dp[i][a]+dp[i][b] + dp[i][s],answer)
    return answer



n=[6,7,6]
s=[4,3,4]
a=[6,4,5]
b=[2,1,6]

fares=[[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
,
[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
]


for i in range(3):
    t = solution(n[i],s[i],a[i],b[i],fares[i])
    print(t)


