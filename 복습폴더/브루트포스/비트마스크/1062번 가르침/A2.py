import sys
sys.stdin=open("00.txt","r")

#https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-1062-%EA%B0%80%EB%A5%B4%EC%B9%A8 참고하기

from itertools import  combinations


#a/c/i/t/n/을 제외한 팔바벳 각각에 고유 번호 부여
bin_dict = {'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14,
            'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7,
            's': 6, 'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y': 1, 'z': 0}

# 알파벳 배열을 2진수로 바꾸어주는 함수

def word_to_bin(word):
    answer = 0b0
    for x in word:
        answer = answer | (1<<bin_dict[x])

    return answer

n,k = map(int,input().split())

words = []

for _ in range(n):
    a = list(input())
    a = set(a[4:-4]).difference('a', 'c', 'i', 't', 'n')
    words.append(a)


if k < 5 :
    print(0)
else :
    bin_list = [word_to_bin(x) for x in words]
    max_count = 0
    power_of_2=[]
    for i in range(21):
        power_of_2.append(2**i)
    print(power_of_2)
    for comb in combinations(power_of_2,k-5):
        current = sum(comb)
        count = 0

        for bin_number in bin_list:
            if bin_number & current == bin_number:
                count+=1

        max_count = max(max_count,count)

    print(max_count)




