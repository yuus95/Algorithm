# algorithm

---


dx = [-1.0.1.0]
dy = [0,1,0,-1]

함수부분 그냥 리턴하면 None 

 ex) def test(a):
      return #그냥리턴은 None



--- 
### 시간복잡도
O(1)<br>O
(N) 1억  
O(NlogN) 5백만  
O(N^2) 1만  
O(N^3) 500  
O(2^N) 20  
O(N!) 10


---
### 나머지연산
(A+B) %M
== (A%M + B%M) %M

(A * B) % M 
== (A%M * B%M) % M

---
### join 함수
ex 'abcd'

join 
''.join(리스트) --> abcd

'구분자'.join(리스트) --> '-'.join(리스트) --> a-b-c-d

ex) a=[1,2,3,4]

print(''.join(map(str,a))) -->1234

---
### reduce함수

- from functools import reduce

reduce(함수, 순서형 자료)

reduce(lambda x,y : x+y,[0,1,2,3,4,])
==> 10

reduce(lambda x,y : y+x,'abced')
==> 'edcba'

reduce(labmda x,y x+y, 이차원배열)
==> 이차원배열 원소를 일차원 배열로 변경시킨다.
[ [0, 0, 0, 0] ,[0,0,0,0] ] ==> [0,0,0,0,0,0,0,0,]

---
### Counter함수
- 카운터함수는 같은 동일한 자료가 몇 개인지 확인하는데 사용한다.

from collections import Counter

ans =[1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]

ans = sorted(list(Counter(ans).values()))
==> 7,8,9  

---
### max함수
dist = [[8, 7, 6, 5, 4, 3], [7, 6, 5, 4, 3, 2], [6, 5, 4, 3, 2, 1], [5, 4, 3, 2, 1, 0]]

ans = [max(row) for row in dist]
print(ans) ==> [8,7,6,5]  // 각 행마다 제일 높은 수가나옴

ans = max([max(row) for row in dist]) 
print(ans) ==> 8  // 2중배열에서 가장 높은 수가 나옴 

---
### 1차원 배열 & 2차원 배열
a[9][9] == > z[81] 표현하는방법

a[x][y] == z[9*x + y]

다시 이차원배열으로 표시

x = z//n 
y = z % n 



---

### 9 * 9 사각형 9등분해서 순서 정하기

``` java
def Squre:
      return (x//3) * 3 + y // 3    
```
---

### set(집합) 연산
```
| 합집합 연산자

& 교집합 연산자

- 차집합 연산자

^ 합집합 - 교집합
```

---
### 매개변수로 배열 사용할 경우
함수를 실행한 뒤 매개변수로 사용된 배열은 변경된 상태로 남는다.
자꾸 까먹는다. 복기하기



---
### 비트마스크 배열에 비트넣기
입력으로 문자열을 받을경우
```python
for i in range(n):
    s = input()
    for x in s:
        words[i] |= (1<< (ord(x)-ord('a')))
```
words배열에는 각문자열에 있는 문자에 해당되는 아스키코드가 비트 형식으로 들어가진다.

---
###순열과 조합
<br/>
순서에 의미가 있는것 --> 순열
nPr 

순서에 의미가 없는 것 --> 조합
n!/(n-r)!*r!


--- 

### DFS 
- 현재값 , 이전값 생각하기 
- 모든 정점들이 연결되어 있는지 확인하기 

---

### Eval()
- 식을 계산해주는 함수 ex) a = '1+2+3' Eval(a) == 6


### 메모제이션
- 한번 계산한 결과를 저장해 두었다가 활용하는 방식으로 중복 계싼을 줄이는 것을 메모제이션이라고 한다.