
def test(n):
    if ( n== 0 ):
        return
    test(n//2)



a = 2

b=test(a)

print(b)