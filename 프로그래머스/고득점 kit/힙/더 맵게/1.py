import heapq

def solution(scoville, K):
    answer = 0
    ok = True
    
    # 힙으로 만들고나서 사용하기
    heapq.heapify(scoville)
    while scoville[0]<K:
        one= heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        heapq.heappush(scoville,one+(two*2))
        answer+=1
        if len(scoville) == 1 and scoville[0] < K:
            ok = False
            break


    if ok :
        return answer
    else :
        return -1





scoville = [1, 2, 3, 9, 10, 12]

k = 7


print(solution(scoville,k))