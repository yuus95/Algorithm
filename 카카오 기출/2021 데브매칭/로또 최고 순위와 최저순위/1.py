
# 6 5 4 3 2 1

def solution(lottos, win_nums):
    max_list = [6,6,5,4,3,2,1]
    res = len([x for x in lottos if x != 0 and x in win_nums])
    zero = len([x for x in lottos if x == 0])

    max_num = max_list[res+zero]
    min_num = max_list[res]


    answer = [max_num,min_num]
    return answer



lottos = [[44, 1, 0, 0, 31, 25]	,[0, 0, 0, 0, 0, 0],[45, 4, 35, 20, 3, 9]]
win_nums = [[31, 10, 45, 1, 6, 19],	[38, 19, 20, 40, 15, 25],[20, 9, 3, 45, 4, 35]]


for i in range(3):
    print(solution(lottos[i],win_nums[i]))
