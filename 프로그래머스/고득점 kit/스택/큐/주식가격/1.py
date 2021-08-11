from collections import deque

def solution(priorities, location):
    q=deque()

    test = 0

    for i in range(len(priorities)):
        q.append((i,priorities[i]))

    while q:
        x,y = q.popleft()
        ok = True
        # for k in range(len(q)):
        #     if y < q[k][1]:
        #         ok = False
        if any(y < b for a,b in q):
                ok = False
                q.append((x, y))
        else:
            test+=1
            if x == location:
                return test


priorities=[[2, 1, 3, 2],[1, 1, 9, 1, 1, 1]]
location=[2,0]


for i in range(2):
    print(solution(priorities[i],location[i]))