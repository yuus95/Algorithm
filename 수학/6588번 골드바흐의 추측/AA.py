import sys
sys.stdin=open("00.txt","r")

MAX = 1000000
check = [0] * (MAX+1)
check[0] = check[1]= True

prime = []

for i in range(2,MAX+1):
    if not check[i]:
        prime.append(i)
        j = i+i
        while j<= MAX:
            check[j] = True
            j+=i

prime= prime[1:] #  문제에서 원하는건 소수의 홀수 prime[0]== 2 은 짝수

while True:
    n = int(input())
    if n == 0 :
        break
    for p in prime:
        if check[n-p] == False:
            print("{0} = {1} + {2}".format(n,p,n-p))
            break




