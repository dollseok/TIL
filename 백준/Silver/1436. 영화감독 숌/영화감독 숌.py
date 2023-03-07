# 백준 1436번 영화감독 숌

'''
666이 들어간 수중에 sort했을 때 N번째 수
'''

# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [0]

for i in range(10):
    lst.append(int(str(i)+'666'))

for j in range(10):
    lst.append(int('666' + str(j)))

for i in range(10):
    for j in range(10):
        lst.append(int(str(i)+'666'+str(j)))
        lst.append(int(str(i)+str(j)+'666'))
        lst.append(int('666'+str(i)+str(j)))

for i in range(10):
    for j in range(10):
        for k in range(10):
            lst.append(int(str(i) + str(j) + str(k) + '666'))
            lst.append(int(str(i) + str(j) + '666' + str(k)))
            lst.append(int(str(i) + '666' + str(j) + str(k)))
            lst.append(int('666' + str(i) + str(j) + str(k)))

for i in range(10):
    for j in range(10):
        for k in range(10):
            for t in range(10):
                lst.append(int(str(i) + str(j) + str(k) + str(t) + '666'))
                lst.append(int(str(i) + str(j) + str(t) + '666' + str(k)))
                lst.append(int(str(i) + str(t) + '666' + str(j) + str(k)))
                lst.append(int(str(t) + '666' + str(i) + str(j) + str(k)))
                lst.append(int('666' + str(t) + str(i) + str(j) + str(k)))

new_lst = list(set(lst))
print(sorted(new_lst)[N])