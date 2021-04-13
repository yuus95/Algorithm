# import sys
# sys.stdin=open("00.txt", "r")

a = input()
data=[]
for x in a :
    if x.isdecimal():
       data.append(int(x))
    else:
        rt =data.pop()
        lt = data.pop()
        if x == '+':
            data.append( lt + rt)
        elif x == '-':
            data.append(lt - rt)
        elif x == '*':
            data.append(lt * rt)
        elif x == '/':
            data.append(lt / rt)

print(data[0])