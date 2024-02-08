import sys
input = sys.stdin.readline

n,m = map(int,input().split())
originlst = []
lowerList=[]

for _ in range(n):
    pocketmon = input().strip()
    originlst.append(pocketmon)
    lowerList.append(pocketmon.lower())

for _ in range(m):
    data = input().strip()
    if data.isdigit():
        print(originlst[int(data)-1])
    else:
        print(lowerList.index(data.lower())+1)