'''
연결 되어있는 숫자 한번에 뒤집기 가능
최소 횟수
'''

data = list(input())
lst = [data[0]]
cnt = 0

for i in range(len(data)-1):
    if data[i] == data[i+1]:
        continue
    else:
        lst.append(data[i+1])

cnt = len(lst)//2
print(cnt)




