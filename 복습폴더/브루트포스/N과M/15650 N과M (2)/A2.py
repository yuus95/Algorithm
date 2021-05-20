import sys
sys.stdin= open("00.txt","r")

#선택버전
n, m =map(int,input().split())

a = [0]  * m

def selected(index,select):
    if select == m :
        for x in a :
            print(x,end=' ')
        print()
        return
    if index > n:
        return

    a[select] = index
    selected(index+1,select+1)
    a[select]= 0
    selected(index+1,select)


selected(1,0)


