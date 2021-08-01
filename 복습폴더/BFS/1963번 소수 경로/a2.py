import sys
from collections import deque
sys.stdin=open("00.txt","r")

#BFS 문제구현 실패


prime = [True] * 10001

def change(num,index,digit):
    if index==0 and digit == 0 :
        return -1
    s = list(str(num))
    s[index] = chr(digit+ord('0'))
    return int(''.join(s))


#에라스토테네스
for i in range(2,10001):
    if prime[i] :
        j = i*i
        while j <= 10000:
            prime[j] = False
            j+=i


n = int(input())

for _ in range(n):
    start ,end = map(int,input().split())

    #이부분을 생각못함
    c=[False] * 10001
    d=[0] * 10001
    d[start] = 0
    c[start]= True

    q=deque()
    q.append(start)
    while q:
        now = q.popleft()
        for idx in range(4):
            for num_idx in range(10):
                nxt = change(now,idx,num_idx)
                if nxt != -1:
                    if prime[nxt] and c[nxt] == False:
                        q.append(nxt)
                        d[nxt] = d[now]+1
                        c[nxt] = True

    print(d[end])