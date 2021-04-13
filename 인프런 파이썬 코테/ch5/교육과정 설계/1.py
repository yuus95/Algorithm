import sys

sys.stdin= open("00.txt","r")


s = input()
n= int(input())

result_box = [0]*(len(s))


data_list = [input() for _ in range(n)]



for i in range(n):
    for x in range(len(data_list[i])):
        for j in range(len(s)):
            if x == s[j]:
                result_box[j] +=1
            if any(result_box[k] == 0 for k in range(j-1)):
                print("NO")
                break
    else :
        print("YES")

