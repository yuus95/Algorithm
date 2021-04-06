import sys
sys.stdin = open("00.txt","r")

a = input()
d1=""
cnt = 0
d2 = ""
sum_list = 0
swich = 0
for i in range(5):
    if a[i].isdecimal():
        d1 +=a[i]
        cnt +=1
    else :
        break

d1 = int(d1)

for i in range(cnt,len(a)):
    if swich  == 1 :
        break
    if a[i] == '-':
        for j in range(cnt+1,len(a)):
            if a[j].isdecimal():
                d2 += a[j]
