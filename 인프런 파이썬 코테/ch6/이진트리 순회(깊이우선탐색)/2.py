#이진트리 순회


#전위 순회
def DFS(x):
    if x > 7:
        return

    else :
        print(x)
        DFS(x+1)
        DFS(x+2)



DFS(1)
