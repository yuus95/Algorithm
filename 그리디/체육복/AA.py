# 프로그래머스 체육복 문제
#오답
def solution(n, lost, reserve):
    ch = [0] * (n + 1)
    ch2 = [0] * (n + 1)
    cnt = 0
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if reserve[i] == lost[j] and ch[lost[j]] == 0 and ch2[reserve[i]] == 0:
                ch2[reserve[i]] = 1
                ch[lost[j]] = 1
                cnt -= 1
            if (reserve[i] - 1 == lost[j] or reserve[i] + 1 == lost[j]) and ch[lost[j]] == 0 and ch2[reserve[i]] == 0:
                ch2[reserve[i]] = 1
                ch[lost[j]] = 1
                cnt += 1

    cnt += n - len(lost)
    print(cnt)
    answer = cnt
    return answer