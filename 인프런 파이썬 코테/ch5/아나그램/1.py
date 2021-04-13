import sys
sys.stdin=open("00.txt","r")


a = input()
b= input()

a_dict = dict()
b_dict=dict()
for x in a :
    a_dict[x] = a_dict.get(x,0)+1

for x in b:
    b_dict[x]=b_dict.get(x,0)+1

for i in a_dict.keys():
    if i in b_dict.keys():
        if a_dict[i] != b_dict[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")