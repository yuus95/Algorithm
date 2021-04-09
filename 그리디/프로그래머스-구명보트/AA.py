import sys
sys.stdin=open("00.txt","r")

people = list(map(int,input().split()))
limit = int(input())

lt = 0
rt = len(people)-1
people.sort()
cnt = 0

while lt<= rt:
    if lt == rt:
        cnt+=1
        break
    if people[lt]+people[rt] <= limit:
        cnt +=1
        lt+=1
        rt-=1
    else:
        rt-=1
        cnt+=1

print(cnt)
