from collections import  deque


def solution(progresses, speeds):
    answer = []

    q = deque()

    for i in range(len(progresses)):
        num = (100-progresses[i])

        temp = num//speeds[i]
        if temp * speeds[i] < num :
            temp +=1

        q.append(temp)

    while q:
        x = q.popleft()
        cnt = 1
        while q:
            if q[0] <= x :
                cnt+=1
                q.popleft()
            else:
                break
        answer.append(cnt)


    return answer




progresses = [[93, 30, 55],[95, 90, 99, 99, 80, 99]]
speeds= [[1, 30, 5],[1, 1, 1, 1, 1, 1]]

for i in range(2):
    print(solution(progresses[i],speeds[i]))