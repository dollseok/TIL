'''
11508 s4

3개의 유제품 사지 않으면 할인 없이 정가 지불

0, 1, 7//3 = 2 , 1 

'''

N = int(input())
l = [int(input()) for _ in range(N)]
l.sort(reverse=True)

r = 0
for i in range(N//3):
    slice_list = l[3 * i : 3 * i + 3]
    #print(slice_list)
    r += sum(slice_list) - slice_list[-1]

if N % 3 == 1:
    r += l[-1]
elif N % 3 == 2:
    r += l[-1] + l[-2]

print(r)