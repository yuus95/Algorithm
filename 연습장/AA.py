from collections import deque


a = 'a_b_c'
b = 'abbbc'

tx1 = []
tx2 = []

for i in range(len(a)) :
    if a[i] == '_':
        continue
    else:
        tx1.append(a[i])
        tx2.append(b[i])
print(tx1,tx2)

if tx1 == tx2:
    print(True)
else:
    print(False)