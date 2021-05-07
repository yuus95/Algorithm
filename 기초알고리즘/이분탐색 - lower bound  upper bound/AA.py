a=list(range(1,11))
l = 6

lt = 0
rt = 9
ans = 0
while lt < rt:

    mid = (lt+rt)//2

    if a[mid] < l :
        lt = mid + 1
        ans = lt
    else :
        rt = mid

print("lower bound",ans)

l = 6
lt = 0
rt = 9
ans = 0

while lt < rt:
    mid = (lt+rt)//2

    if a[mid] <= l :
        lt = mid + 1
        ans = lt
    else :
        rt = mid

print("upper bound",ans)