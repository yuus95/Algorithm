
import  heapq
def solution(operations):
    answer = []
    q = []
    minus_q = []
    for i in range(len(operations)):
        input , num = operations[i].split()
        num = int(num)
        if input == "I":
            heapq.heappush(q,num)
            heapq.heappush(minus_q,-num)
            answer.append(num)

        else:
            if len(q) > 0 :
                if num == 1:

                    heappop = heapq.heappop(minus_q)
                    q.remove(-heappop)
                    answer.remove(-heappop)
                else:
                    heapq_heappop = heapq.heappop(q)
                    minus_q.remove(-heapq_heappop)
                    answer.remove(heapq_heappop)

    if len(answer) == 0 :
        return [0,0]

    else :
        return [-heapq.heappop(minus_q),heapq.heappop(q)]

operations= [["I 16","D 1"],["I 7","I 5","I -5","D -1"]]

for i in range(2):
    print("aa",solution(operations[i]))