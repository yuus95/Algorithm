def DFS(v):
    if v>7:
        return
    else:
        #전위 순회 방식 - 대표적인 방식
        # print(v,end=' ')
        # DFS(v*2)
        # DFS(v*2+1)

        #중위순회 출력
        # DFS(v * 2)
        # print(v, end=' ')
        # DFS(v * 2 + 1)

        #후위순회 출력 -대표 병합정렬
        DFS(v * 2)
        DFS(v * 2 + 1)
        print(v, end=' ')
DFS(1)