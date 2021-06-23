import sys

sys.stdin=open("00.txt","r")

def DFS(sum,cc):
    global amount_cnt
    if (cc==0):
        return
    print(sum,"sum")
    if sum > amount :
        return
    if sum == amount:
        amount_cnt+=1
    else :
        for i in range(count):
            if ch[data_list[i]] != 0 :
                ch[data_list[i]] -=1
                DFS(sum+data_list[i],cc-1)
                ch[data_list[i]] += 1





amount = int(input())
amount_cnt = 0
count = int(input())

data_list = [0] * count
ch =[0]*11

for i in range(count):
    a,b = map(int,input().split())
    data_list[i] = a
    ch[a]=b

last_num = sum(ch)
DFS(0,last_num)

print(amount_cnt)
