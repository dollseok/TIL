def solution(phone_book):
    phone_book.sort()
    l = len(phone_book)
    for i in range(l-1):
        pre = phone_book[i]
        data = phone_book[i+1]

        for k in range(len(pre)):
            if pre[k] != data[k]: # 다르면 접두사가 아님
                break
            else:
                if k == len(pre)-1: # 접두사면
                    return False
    
    return True