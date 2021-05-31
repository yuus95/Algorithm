import sys

sys.stdin=open("00.txt","r")


n= int(input())
a = [''] * n

letters = set()
for i in range(n):
    a[i]=input()
    letters |= set(a[i])

print(a)
print(letters)

letters = list(letters)

print(letters)