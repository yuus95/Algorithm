import sys
sys.stdin=open("00.txt","r")

MAX= 10000000

ch =  [0] *(MAX+1)

ch[0] = ch[1] = True

n , m = map(int,input().split())

for i in range(2,m+1):
    if ch[i] == False :
         j=2
         while i*j <= m+1:
             ch[i*j] = True
             j+=1

for i in range(n,m+1):
    if ch[i] == False:
        print(i)
