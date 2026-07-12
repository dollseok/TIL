def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        l = array[i-1:j]
        l.sort()
        answer.append(l[k-1])
                
    return answer