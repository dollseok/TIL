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