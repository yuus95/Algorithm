def binary(n):
    if n == 0:
        return
    else:
        binary(n//2)
        print(n%2,end ='')




n = int(input())

binary(n)