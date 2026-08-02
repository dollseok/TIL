def solution(keymap, targets):
    
    key_dict = {}
    for s in keymap:
        for i in range(len(list(s))):
            key = s[i]
            if key in key_dict:
                key_dict[key] = min(key_dict[key], i + 1)
            else:
                key_dict[key] = i + 1
    answer = []
    for target in targets:
        n = 0
        for t in target:
            if t in key_dict:
                n += key_dict[t]
            else:
                n = -1
                break
        
        answer.append(n)
        
    return answer