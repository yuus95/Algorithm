import sys
sys.stdin=open("00.txt","r")

# 시간복잡도 N제곱
n = 9
a = [int(input()) for _ in range(n)]
a.sort()
total = sum(a)

for i in range(0,n):
    for j in range(i+1,n):
        if total - a[i] - a[j] == 100:   # 시간복잡도 N제곱  일곱 난쟁이 키의 합은 미리 구한 키의 합에서 제외하기로 한 두 난쟁이의 키를 뺴면 된다. 이 부분은 수식으로 구할 수 있기 떄문에 O(1)이다.
            for k in range(0,n):
                if i == k or j == k:
                    continue

                print(a[k])
            sys.exit(0)