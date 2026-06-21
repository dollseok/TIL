def solution(s):
    answer = ''
    word_index = 0
    l = list(s)
    
    for ch in s:
        if ch == ' ':
            answer += ch
            word_index = 0
        else:
            if word_index % 2 == 0:
                answer += ch.upper()
            else:
                answer += ch.lower()
            word_index += 1
        
    
    return answer