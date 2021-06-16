import sys

sys.stdin=open("00.txt","r")

n,s = map(int,input().split())

a = list(map(int,input().split()))

#부분수열 나누기
m = n//2

n = n-m

#부분수열의 갯수 2* n-m개
first = [0] * (1<<n)


#비트 마스크를 이용한 부분수열 구하기
for i in range(1<<n):
    for k in range(n):
        if (i&(1<<k))>0:
            first[i] += a[k]



#뒤에있는 m/2  부분수열구하기
second = [0] * (1<<m)
for i in range(1<<m):
    for k in range(m):
        if (i&(1<<k)) > 0:
            second[i] +=a[k+n]

# sort복잡도 O(Nlogn)
first.sort()
second.sort()
second.reverse()

#부분 수열 갯수
n = (1<<n)
m = (1<<m)

i = 0
j = 0
ans = 0
while i < n and  j < m :
    if first[i] + second[j] == s:
        c1 = 1
        c2 = 1
        i +=1
        j +=1
        while i < n and first[i] == first[i-1]:
            c1 +=1
            i += 1
        while j < m and second[j] == second[j-1]:
            c2 +=1
            j += 1

        ans += c1 * c2

    elif first[i] + second[ j] < s:
        i += 1

    else:
        j +=1

if s == 0 :
    ans -= 1
print(ans)




