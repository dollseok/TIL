def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for s in babbling:
        idx = 0
        previous = ""
        
        while idx < len(s):
            matched = False
            for word in words:
                if s.startswith(word,idx) and word != previous:
                    idx += len(word)
                    previous = word
                    matched = True
                    break
            if not matched:
                break
        
        if idx == len(s):
            answer += 1
                
    
    return answer