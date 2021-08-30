from collections import deque

# 1478
def solution(s):
    num_key = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    s = deque(s)

    stack = ""
    answer = ""
    while s:
        x = s.popleft()
        if x.isalpha():
            stack+=x
            if stack in num_key.keys():
                answer+=str(num_key[stack])
                stack =""
        else:
            answer+=str(x)





    return int(answer)


s=["one4seveneight","23four5six7","2three45sixseven","123"]

for i in range(len(s)):
    print(solution(s[i]))