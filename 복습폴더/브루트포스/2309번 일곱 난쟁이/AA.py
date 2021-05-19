import sys
sys.stdin=open("00.txt","r")


a = []

for _ in range(9):
    a.append(int(input()))

a.sort()

cp = sum(a)

ok = True
for i in range(9):
    if ok == False:
        break
    for j in range(i+1,9):
        if ok == False:
            break
        if cp - a[i] - a[j] == 100:
            for k in range(9):
                if k == i or k == j :
                    continue
                print(a[k])
            ok = False
            break



