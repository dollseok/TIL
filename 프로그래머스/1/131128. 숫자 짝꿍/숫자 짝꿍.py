def solution(X, Y):
    answer = []
    
    x = sorted(list(X),reverse=True)
    y = sorted(list(Y),reverse=True)
    
    x_idx = 0
    y_idx = 0
    
    while (x_idx != len(x) and y_idx != len(y)):
        
        if x[x_idx] == y[y_idx]:
            answer.append(x[x_idx])
            x_idx += 1
            y_idx += 1
        elif x[x_idx] < y[y_idx]:
            y_idx += 1
        else:
            x_idx += 1
    
    result = ''.join(answer)
    
    if result == '':
        return "-1"
    if set(result) == {'0'}:
        return '0'
    
    return result