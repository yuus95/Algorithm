import sys
sys.stdin=open("00.txt","r")
#5 1 2

n = int(input())
a = list(map(int,input().split()))
c = [False] *(n*20 +10)


#(2^n) - 1  만큼 경우의수 생성 (ex n == 3 이면 이진수 3비트 까지 합은 7이므로 (2^n)  - 1
for i in range(1<<n):
    print("i", i)
    s = 0
    for j in range(n):
        print("=======================")
        if (i & (1<<j)): #비트 한자리씩 계산  i== 3 일 경우(비트)  i<<0의 1 과  i<<1 의 10 이 포함할 수 있으므로  a = > a [0] + a[1]
            s+= a[j]
    c[s] = True

print(c)

