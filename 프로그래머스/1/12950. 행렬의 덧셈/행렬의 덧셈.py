def solution(arr1, arr2):
    y = len(arr1)
    x = len(arr1[0])
    answer = []
    
    for i in range(y):
        l = [0]*x
        for j in range(x):
    
            l[j] = arr1[i][j] + arr2[i][j]
        answer.append(l)
    return answer