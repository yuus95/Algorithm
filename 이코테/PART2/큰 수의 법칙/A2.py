import  sys
sys.stdin=open("00.txt")

# 효율적인 답안

N,M,K = map(int,input().split())

a = list(map(int,input().split()))

a.sort()

sum = 0
first = a[-1]
second = a[-2]

count = M //(K+1)

sum += second*count
count += M % (K+1)
sum += first*count*K

print(sum)
