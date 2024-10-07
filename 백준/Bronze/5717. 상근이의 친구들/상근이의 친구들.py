while True:
    ls = list(map(int,input().split()))
    if ls == [0,0]:
        break
    print(sum(ls))