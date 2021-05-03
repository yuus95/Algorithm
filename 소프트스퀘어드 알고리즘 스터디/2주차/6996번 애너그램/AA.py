import sys
sys.stdin=open("00.txt")

n = int(input())
for _ in range(n):
    a,b =input().split()
    a_list = []
    b_list = []
    if len(a) != len(b):
        print("{} & {} are NOT anagrams.".format(a,b))
    else:
        for i in range(len(a)):
            a_list.append(ord(a[i]))
        for i in range(len(b)):
            b_list.append(ord(b[i]))
        a_list.sort()
        b_list.sort()
        for i in range(len(a_list)):
            if a_list[i] != b_list[i]:
                print("{} & {} are NOT anagrams.".format(a,b))
                break
        else :
            print("{} & {} are anagrams.".format(a, b))