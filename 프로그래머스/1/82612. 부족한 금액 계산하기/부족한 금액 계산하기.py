def solution(price, money, count):
    need = 0
    for i in range(1,count+1):
        need += i * price
        
    if money - need >= 0:
        return 0
    else:
        return need - money