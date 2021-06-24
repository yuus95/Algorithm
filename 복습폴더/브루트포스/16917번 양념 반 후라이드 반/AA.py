import sys
sys.stdin=open("00.txt","r")


a,b,c,x,y = map(int,input().split())


# 반반 없이 사는 경우
ans = a * x + b * y

# 반마리 살 수 있는 최대 수
num = min(x,y)


#반마리갯수를 (0~num 까지 계산)
for i in range(1,num+1):
    
    # 최소갯수니깐 넘어도 상관없음
    temp = (i * c * 2 ) + ((x-i)* min(2*c,a)) + ((y-i) * min(2*c,b))

    # temp값과 ans값 비교해서 작은값을 ans로 넣기기
    if temp < ans :
        ans = temp

print(ans)