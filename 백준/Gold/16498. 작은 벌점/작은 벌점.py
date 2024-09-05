'''

세명이 한팀이 되어 정수를 조합하는 게임이 있다.

'''

a,b,c = map(int,input().split())

alist = sorted(list(map(int,input().split())))
blist = sorted(list(map(int,input().split())))
clist = sorted(list(map(int,input().split())))


def parasearch(target,ls):
    s = 0
    e = len(ls) - 1
    nearest = ls[(s+e)//2]
    while s <= e:

        mid = (s+e)//2
        if ls[mid] < target:
            s = mid + 1
        elif ls[mid] > target:
            e = mid - 1
        else:
            return target

        if abs(ls[mid] - target) < abs(nearest - target):
            nearest = ls[mid]

    return nearest

def cal(a,b,c):
    return abs(max(a,b,c) - min(a,b,c))

result = 10000000000000
for a in alist:
    # print(a)
    b = parasearch(a, blist)
    # print(b,blist)
    c1 = parasearch(a, clist)
    # print(c1,clist)
    c2 = parasearch(b,clist)
    # print(c2,clist)

    result = min(cal(a,b,c1),cal(a,b,c2),result)

print(result)


'''
1 3 4
9
2 5 100
1 6 7 10

4
'''