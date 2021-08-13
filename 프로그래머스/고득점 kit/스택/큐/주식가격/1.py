from collections import deque

def solution(prices):
    answer = []
    q= deque()

    for i in range(len(prices)):
        q.append(prices[i])

    while q:
        x = q.popleft()
        cnt = 0
        for temp in q:
            cnt +=1
            if x > temp:
                break
        answer.append(cnt)
    return answer


prices=[1, 2, 3, 2, 3]


print(solution(prices))