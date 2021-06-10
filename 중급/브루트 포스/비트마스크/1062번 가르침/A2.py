import sys
sys.stdin=open("00.txt","r")


n,k = map(int,input().split())

def count(a):
    ok = True


def go(index,k,a):

    if index == 26:
        if k == 6:
            count(a)
    if k >= 6:
        return
    if index in a:
        go(index+1,k,a)
    else:
        go(index+1,k+1,a+[index])
        go(index+1,k,a)
    return

# words=[]
# # for _ in range(n):
# #     words.append(input())

words=  [input() for _ in range(n)]
box = ['a','n','t','c','i']
word_box = []

for i in range(5):
    word_box.append(ord(box[i])-ord('a'))


for word in words:
    a = set(word)
    temp = []
    for x in a :
        temp.append(ord(x)-ord('a'))
    word_box.append(temp)

go(0,0,box)