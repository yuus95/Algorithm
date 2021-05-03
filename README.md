# algorithm

dx = [-1.0.1.0]
dy = [0,1,0,-1]

함수부분 그냥 리턴하면 None 

 ex) def test(a):
      return #그냥리턴은 None


===========시간복잡도 ==============
O(1)
O(N) 1억
O(NlogN) 5백만
O(N^2) 1만
O(N^3) 500
O(2^N) 20
O(N!) 10

=========== 나머지연산 ==============

(A+B) %M
== (A%M + B%M) %M

(A * B) % M 
== (A%M * B%M) % M

=========== join 함수 ==============
ex 'abcd'

join 
''.join(리스트) --> abcd

'구분자'.join(리스트) --> '-'.join(리스트) --> a-b-c-d

ex) a=[1,2,3,4]

print(''.join(map(str,a))) -->1234

