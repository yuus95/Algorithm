
#  |r1 - r2| + |c1 - c2| 입니다. ↩
# PooP
# PxP , PxxP

# P o
# o P

# p
# o
# o
# p
def check(check_arr,place):
    n = len(check_arr)

    if n == 0 :
        return 1

    for i in range(n-1):
        x1, y1 = check_arr[i][0], check_arr[i][1]
        for j in range(i+1,n):
            x2,y2 = check_arr[j][0],check_arr[j][1]

            dis = abs(x1-x2) +abs(y1-y2)
            if dis <= 2:
                if x1 == x2:
                    if y1 < y2 :
                        y = y1
                    else :
                        y= y2


                    if abs(y1-y2) == 2 and not(place[x1][y+1] == 'X' or place[x1][y+2] =='X'):
                        return False
                    elif abs(y1-y2) ==1 and  place[x1][y+1] != 'X':
                        return False
                elif y1 == y2 :
                    if x1 < x2:
                        x = x1
                    else :
                        x = x2

                    if abs(x1-x2) == 2 and not(place[x+1][y1]=='X' or place[x+2][y1] == 'X'):
                        return False
                    elif abs(x1-x2) == 1 and place[x+1][y1] != 'X':
                        return False
                else :
                    if y1 < y2 :
                        if place[x1][y1+1] != 'X' or place[x2][y2-1] != 'X':
                            return False
                    else :
                        if place[x1][y1-1] != 'X' or place[x2][y2+1] != 'X':
                            return False


    return True




def solution(places):
    answer = []

    for place in places :

        check_arr = []

        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    check_arr.append((x,y))
        if check(check_arr,place):
            answer.append(1)
        else :
            answer.append(0)

    return answer

places =[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))