genres = ["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]



def solution(genres, plays):
    answer = []
    a={}
    for i in range(len(genres)):
        if genres[i] in a :
            a[genres[i]].append((plays[i],i))
        else:
            a[genres[i]] = [(plays[i],i)]

    sum_list={}

    for k in a:
        temp = 0
        for x,y in a[k]:
            temp+= x
        sum_list[k]=temp

    l  = sorted(sum_list,key=lambda x: -sum_list[x])

    for alpha in l :
        sorted1 = sorted(a[alpha], key= lambda x: (-x[0],x[1]))
        answer.append(sorted1[0][1])
        if len(sorted1) > 1 :
            answer.append(sorted1[1][1])

    return answer




print(solution(genres,plays))