import sys
sys.stdin=open("00.txt","r")

n,m,r = map(int,input().split())

num = min(n,m) //2

a = [list(map(int,input().split())) for _ in range(n)]


groupn = []

for k in range(num):
    group = []
    for j in range(k, m-k):
        group.append(a[k][j])
    for i in range(k+1,n-k-1):
        group.append(a[i][m-k-1])
    for j in range(m-k-1,k,-1):
        group.append(a[n-k-1][j])
    for i in range(n-k-1,k,-1):
        group.append(a[i][k])
    groupn.append(group)

for k in range(len(groupn)):
    l = len(groupn[k])
    group = groupn[k]
    index = r%l

    for j in range(k,m-k):
        a[k][j] = group[index]
        index= (index+1) % l

    for i in range(k+1,n-k-1):
        a[i][m-k-1] = group[index]
        index = (index + 1) % l

    for j in range(m-k-1,k,-1):
        a[n-k-1][j] = group[index]
        index = (index + 1) % l

    for i in range(n-k-1,k,-1):
        a[i][k] = group[index]
        index = (index + 1) % l

for x in a :
    print((' '.join(map(str,x))))