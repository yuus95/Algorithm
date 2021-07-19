import sys
sys.stdin=open("00.txt","r")
n = int(input())
# 내구도
s = [0]*n
# 무게
w = [0]*n
for i in range(n):
    s[i], w[i] = map(int, input().split())

# 손에 index번 계란을 들었을 경우  -> n-1번째 계란을 들었을 경우 답구하기
def go(index):
    if index == n:
        cnt = 0
        #깨진 계란의 갯수 리턴
        for i in range(n):
            if s[i] <= 0:
                cnt += 1
        return cnt
    #이미 깨져있을 경우
    if s[index] <= 0:
        return go(index+1)
    ans = 0
    # ok == True index번 계란으로 다른 계란을 칠 수 있다.
    ok = False
    #현재 index번 계란으로 칠 계란 J번을 찾기
    for j in range(n):
        i = index
        #  자기 자신일 경우 무시
        if i == j:
            continue
        if s[j] > 0: # j번째 계란이 깨지지 않음
            ok = True
            s[i] -= w[j]
            s[j] -= w[i]
            temp = go(index+1)
            if ans < temp:
                ans = temp
            s[i] += w[j]
            s[j] += w[i]
            
    # 인덱스 외에 나머지 모두 깨졌을 경우 다음함수 호출
    if not ok:
        return go(index+1)
    return ans

print(go(0))
