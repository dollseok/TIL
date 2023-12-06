import sys

N, K = map(int, input().split())

numLst = []
resLst = []

for i in range(1,N+1):
    numLst.append(i)

ord = K
while numLst:
    if len(numLst) < ord:
        ord = ord - len(numLst)
    else:
        resLst.append(str(numLst[ord - 1]))
        numLst = numLst[ord:] + numLst[0:ord-1]
        ord = K

res = ", ".join(resLst)

print(f'<{res}>')

