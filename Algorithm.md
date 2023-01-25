# BAEKJOON

## 새싹

### 10172번 : 개
https://www.acmicpc.net/problem/10172
<br/>

* \를 붙여줘야 \ , " 같은 특수 문자가 프린트 된다.

```python
#input

print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")
```
```bash
#output

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop
$ python test.py
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
```
---

## BRONZE V

### 1000번 : A+B
https://www.acmicpc.net/problem/1000

- 입력을 가로로 했어야 했음.
```python
#input

a,b = input().split()
print(int(a) + int(b))
```
```bash
1 2 #입력
3 #출력
```
### 10952번 : A+B -5
https://www.acmicpc.net/problem/10952
- 계속 마지막에 0이 프린트 되서 오류
- A,B 를 둘다 int로 조건문에서 받아줘야함
- 그래야 0이 마지막에 출력되지 않음
```python
while True:
    A,B = input().split()
    if int(A) == 0 and int(B) == 0 :
        break
    else :
        print(int(A)+int(B))
```

### 9086번 : 문자열
https://www.acmicpc.net/problem/9086
- 가장 양끝의 문자열을 출력하는 문제
- input의 첫번째에 숫자가 주어지는만큼 개수가 주어지는데, 그것을 첫 반복 값으로 받는다

```python
n = int(input())
for i in range(n):
    a = input()
    print(a[:1]+a[-1:])
```
```python
n = int(input())
for i in range(n):
    a = input()
    print(f'{a[:1]}{a[-1:]}')
```


## Bronze IV

### 2742번 기찍 N (반대로 찍기)
https://www.acmicpc.net/problem/2742


```python
a = int(input())

for i in range(a) :
    print(a-i)
```

### 15552번 빠른 A+B
https://www.acmicpc.net/problem/15552
- import sys로 해서 stdin.readline()를 사용해야 시간 초과가 안남
- 사실 이 개념을 아직 잘 모름

```python
import sys

T = int(input())
for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
```

### 11720번 숫자의 합
https://www.acmicpc.net/problem/11720
- 덩어리 숫자를 나누는 방법
- 무조건 리스트를 새로 만들기보다는 sum을 사용할 것

```python
T = int(input())
list = list(str(input())) # 하나의 덩어리 숫자를 각 자리수로 나눈다(리스트화)
sum = 0
for i in list:
    sum += int(i)

print(sum)
```

### 2480번 주사위 세개

```python
a,b,c = map(int,input().split()) # 한줄로 들어온 세개의 수를 각각 나눈다. 그리고 int 정수화 시킨다.

if a == b and b == c and c == a :
    print(10000 + a*1000)
elif a == b and a != c :
    print(1000 + b*100)
elif a == c and a != b :
    print(1000 + a*100)
elif b == c and a != b :
    print(1000 + b*100)
elif a != b and b != c and c != a :
    print((max(a,b,c)) * 100)  # a,b,c 각각 int로 있으면 max사용 가능
```


### 5543번 상근날드

https://www.acmicpc.net/problem/5543

```python
menu_list = []
#문제를 읽고 애초에 메뉴가 5개라 range를 5로 설정
for i in range(5) :
    a = int(input())
    menu_list.append(a)

burger = [menu_list[0] , menu_list[1], menu_list[2]]
burger.sort()


drink = [menu_list[3] , menu_list[4]]
drink.sort()

print(burger[0] + drink[0] - 50)

```

### 10808번 알파벳 개수

https://www.acmicpc.net/problem/10808

```python
all_word = 'abcdefghijklmnopqrstuvwxyz'

# print(list(all_word))

a = input()

for element in list(all_word):
    cnt = a.count(element)
    print(cnt, end = ' ')
# 각 글자들의 개수를 확인해서 end를 한줄 내리는 것이 아닌 한칸 띄우는 것으로 출력
```


### 2845번 파티가 끝나고 난 뒤

https://www.acmicpc.net/problem/2845

```
input 
5 20
99 101 1000 0 97
```
```
output
-1 1 900 -100 -3
```

```python
p, sq = map(int,input().split())
# print(p*sq)

news = list(map(int,input().split()))
# print(news)

result_lst = []
for i in news:
    a = (i - (p*sq))
    print(a, end= ' ')
```

### 11365번 !밀비 급일(일급 비밀!)

https://www.acmicpc.net/problem/11365

- 참고 사이트
- https://itholic.github.io/python-reverse-string/

```
input
!edoc doog a tahW
noitacitsufbo
erafraw enirambus detcirtsernu yraurbeF fo tsrif eht no nigeb ot dnetni eW
lla sees rodroM fo drol eht ,ssertrof sih nihtiw delaecnoC
END
```
```
What a good code!
obfustication
We intend to begin on the first of February unrestricted submarine warfare
Concealed within his fortress, the lord of Mordor sees all
```

```python
while True:
    a = input()
    message = []

    if a == 'END' :
        break

    b = list(a)

    for i in range(len(b)) :
        message.append(b[len(a)-i-1])

    real_message = ''.join(message)

    print(real_message)
```
```python
# 또 다른 짧은 풀이

while True :
    a = input()
    if a == 'END' :
        break
    print(a[::-1])

# 역순으로 출력하기
```

### 2941번 크로아티아 알파벳

https://www.acmicpc.net/problem/2941

```python
cro_word = input()
cro_alpha= ['s=','lj' , 'dz=' , 'nj' , 'd-', 'z=', 'c-' , 'c=']

for i in cro_alpha:
    cro_word = cro_word.replace(i,'.')

print(len(cro_word))

# 문제에 따라서 dz= 과 순서를 조금 바꿔줬어야 했다.
# find로 찾아서 있는지 없는지에 따라서 바꾸려했지만 'lj'가 안 먹히는 문제가 있었다.
```



