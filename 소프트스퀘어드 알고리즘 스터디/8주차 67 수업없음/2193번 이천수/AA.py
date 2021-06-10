n = int(input())


d = [0] * 91

d[1] = 1


for i in range(2,91):

    if i == 2 :
        d[i] += 1
    else:
        d[i] = d[i-1] +  d[i-2]


print(d[n])
