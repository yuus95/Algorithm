n , k = map(int,input().split())

d_list = []
i = 0
cnt = 0
for _ in range(n):
    d_list.append(int(input()))

d_list.sort(reverse=True)

while k >0:
    cnt += k //d_list[i]
    k = k%d_list[i]
    i+=1

print(cnt)