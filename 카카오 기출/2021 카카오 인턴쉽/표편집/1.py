# OOOOXOOO
# OOXOXOOO

def solution(n, k, cmd):
    answer = ''
    temp = ['O'] * n
    stack = []
    for i in range(len(cmd)):

        # 삭제 또는 복구
        # 맨끝칸 삭제할 경우 위에칸 바라보기
        if len(cmd[i]) == 1:
            if cmd[i] == 'Z':
                if len(stack) >= 1 :
                    num = stack.pop()
                    temp[num] = 'O'
            else :
                temp[k] = 'X'
                stack.append(k)

                if k == len(temp):
                    for j in range(k,-1,-1):
                        if temp[j] =='O':
                            k = j
                            break
                else :
                    ok = False
                    for j in range(i+1,len(temp)):
                        if temp[j] =='O':
                            k = j
                            ok = True
                            break

                    if not ok :
                        for j in range(k, -1, -1):
                            if temp[j] == 'O':
                                k = j
                                break



        
        # 올리기 아니면 내리기
        else :
            x,y, = cmd[i].split()
            y = int(y)
            if x == 'D':
                if k == len(temp) :
                    continue
                elif k +y >= len(temp):
                    for j in range(len(temp)-1,k,-1):
                        if temp[j] == 'O':
                            k = j
                            break
                else:
                     for j in range(k+y,len(temp)):
                         if temp[j] == 'O':
                             k = j
                             break


            else :
                if k == 0 :
                    continue
                elif k - y < 0 :
                    for j in range(k):
                        if temp[j] == 'O':
                            k = j
                            break
                else :
                    for j in range(k-y,-1,-1):
                        if temp[j] == 'O':
                            k = j
                            break

            

    return "".join(temp)


n = [8,8]
k = [2,2]
cmd = [["D 2","C","U 3","C","D 4","C","U 2","Z","Z"],["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]]


for i in range(2):
    print(solution(n[i],k[i],cmd[i]))