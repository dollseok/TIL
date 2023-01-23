# SWEA

## D1

### 2070번. 큰 놈, 작은 놈, 같은 놈
--- 
- 아직 첫번째 input 숫자 하나로 받는 것 그리고 뒤에 연속으로 나오는 input을 map과 split으로 받는 것 기억하기

```python

#input
'''
3
3 8 
7 7 
369 123      

'''

T = int(input()) 
    #첫번째 input을 받음
for test_case in range(1, T + 1): 
    # 받은 input으로 range 설정
    a,b = map(int,input().split()) 
    # 후에 각 input을 나누어서 받음
   
    if a > b:
        print(f'#{test_case} >')
    elif a < b:
        print(f'#{test_case} <')
    else :
        print(f'#{test_case} =')


'''        
#1 <
#2 =
#3 >
'''

```

### 2056번 연월일 달력
- Q. 연월일 순으로 구성되 8자리 숫자가 주어진다. 그 숫자를 0000/00/00의 형태로 바꾸고 오류라면 -1을 표시, 각 출력 앞에 각 테스트 케이스 t에 대하여 #t를 찍고 한칸 띄워 출력.


```python
T= int(input())

for test_case in range(1,T+1)
    a = list(str(input()))  #각 자리수마다 나누기 위해 str 문자화
    year = a[0] + a[1] + a[2] + a[3]
    month = a[4] + a[5]
    day = a[6] + a[7]

    if int(month) > 12 or int(month) <= 0 :
        print(f'#{test_case} -1')
        # 월이 1-12사이가 아닐때 오류 

    elif int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12 :
        if int(day) > 31 or int(day) <= 0:
            print(f'#{test_case} -1')
        else :
            print(f'#{test_case} {year}/{month}/{day}')

            # 각 일수가 31일이 넘어버릴 때 오류 -1

        
    elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11 :
        if int(day) > 30 or int(day) <= 0:
            print(f'#{test_case} -1')
        else :
            print(f'#{test_case} {year}/{month}/{day}')

            # 각 일수가 30 일이 넘어버릴때 오류 -1
        
    elif int(month) == 2:
        if int(day) > 28 or int(day) <= 0:
            print(f'#{test_case} -1')
        else :
            print(f'#{test_case} {year}/{month}/{day}')

            # 2월이니 28일이 넘어버릴때 오류 -1
```

### 2050번 알파벳을 숫자로 변환
- 다시 풀기

- Q. 알파벳으로 이루어진 문자열을 입력받아 각 알파벳을 1부터 26까지 숫자로 변환하여 출력하여라


### 1933번 N의 약수
- Q. 정수 N의 약수를 오름차순으로 출력하는 프로그램

```python
a = int(input())
list = []
for i in range(1,a+1)
    if a % i == 0:
        list.append(i)

for n in list :
    print(n, end = ' ')
# 프린트 할 때 , 없이 한줄로 프린트 하는 코드 중요!
```


