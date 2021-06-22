import sys
sys.stdin=open("00.txt","r")


a = input()

# start end last index?
last = -1
num = 0
res = 0

for i in range(len(a)):

    if i == 0 :
        if a[i] == 'c' :
            num = 26
        else :
            num = 10
        res = num
    else:
        if a[i] =='c':
            if a[i] == a[last]:
                num = 25
            else:
                num =26
        else :
            if a[i] == a[last]:
                num = 9
            else:
                num = 10
        res *=num
    last = i

print(res)