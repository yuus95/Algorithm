#못풀었다. 다시풀기
def solution(name):
    # z = 90 a = 65
    num = -1
    for i in name:
        if i == 'A':
            continue
        else:
            num += 1
        res1 = ord(i) - 65
        res2 = 91 - ord(i)

        if res1 > res2:
            num += res2
        else:
            num += res1

    print(num)
    return num