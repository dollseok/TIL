'''
IOIOI
'''

n = int(input())
m = int(input())
data = input()

i = 0
cnt = 0
result = 0

while i < (m-1):
    if data[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            result += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(result)