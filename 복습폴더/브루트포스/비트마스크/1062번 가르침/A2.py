import sys
sys.stdin=open("00.txt","r")
#다시풀기

n, m = map(int,input().split())
words=[0] * n
mask = 0
answer = 0
countt= 0
# [663813, 551317, 663813
for i in range(n):
    s = input()
    for x in s:
        words[i] |= (1<< (ord(x)-ord('a')))


for i in ['a','n','t','i','c']:
    mask |= (1<< ord(i)-ord('a'))





def go(index,k,mask,words):
    global answer, countt
    if k- 5 <0 :
        temp = count(mask,words)
        if answer < temp :
            answer = temp
        return
    if index == 26:
        return
    if index in [ord('a')-ord('a'),ord('n')-ord('a'),ord('t')-ord('a'),ord('i')-ord('a'),ord('c')-ord('a')]:
        countt+=1
        go(index+1,k,mask,words)

    else :
        go(index + 1, k-1, mask |1<<index, words)
        go(index + 1, k, mask, words)



go(0,m,0,words)

print(countt)
print(answer)