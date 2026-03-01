'''


1 2 3 4 5
1 2 3 4 5

'''

N = int(input())
m_list = list(map(int,input().split()))
m_list.sort()

biggest = -1
if N % 2 == 1:
    biggest = m_list.pop()
    N = N - 1


r_list = []
for i in range(N // 2):
    r_list.append(m_list[i] + m_list[N - 1 - i])

if biggest:
    r_list.append(biggest)

print(max(r_list)) 