'''
IOIOI
'''

n = int(input())
m = int(input())
data = input()


P = 'I'
for i in range(n):
    P = P + 'OI'

cnt = 0

for i in range(m-len(P)+1):
    compare_ = ''
    if data[i] == 'I':
        for j in range(len(P)):
            compare_ += data[i+j]
            if compare_ == P:
                cnt += 1

print(cnt)
