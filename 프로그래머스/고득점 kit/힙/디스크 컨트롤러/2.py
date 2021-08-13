# 실패 내일 다시 풀기
def solution(jobs):
    answer = 0
    n = len(jobs)
    data = sorted(jobs,key=lambda x:(x[1],x[0]))
    sum = 0
    temp = 0
    for i in range(len(data)):
        sum += data[i][1]
        temp += sum - data[i][0]

    answer = temp//n


    return answer



print(solution([[0, 3], [1, 9], [2, 6]]))