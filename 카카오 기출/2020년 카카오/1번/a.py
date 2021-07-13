strs= ["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]



# 가장 짧은 문자열 길이
# 길이는 최대반
# 문자열 전체에 대해 검사
# 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
# 문자는 앞에서 하나씩 체크
# 브루트포스 하나씩 다해봐야함
#

#aabbaccc  2abbaccc 2a2baccc 2a2ba3c


def solution(s):
    answer = 0
    n = len(s)
    result = []

    if n == 1 :
        return 1

    # 검사 문자열 길이
    for i in range(1,(n//2)+1):
        temp = ""
        count = 1
        str_s = s[:i]
        for j in range(i,n,i):
            if i + j > n+1:
                continue
            if str_s == s[j:j+i]:
                count+=1
            else :
                if count == 1 :
                    count= ""
                temp += str(count)+str_s
                str_s = s[j:j+i]
                count = 1
        # 마지막에 비교한 값이 count가 증가하고 끝날 경우 str_s에 들어가질 못함. ㄴ
        if count == 1 :
            count = ""
        temp += str(count)+str_s
        result.append(len(temp))

    return min(result)





for s in strs:
    print(solution(s))

