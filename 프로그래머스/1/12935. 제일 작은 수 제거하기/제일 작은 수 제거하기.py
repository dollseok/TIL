def solution(arr):
    
    
    i = arr.index(min(arr))
    arr.pop(i)
    
    if arr == []:
        return [-1]
    return arr
    