def solution(s, skip, index):
    alphabet = [
        chr(i)
        for i in range(ord('a'), ord('z') + 1)
        if chr(i) not in skip
    ]
    answer = ''
    # for i in range(ord('a'), ord('z')+1):
    #     print(i,chr(i), ord(chr(i)))
    
    for char in s:
        current = alphabet.index(char)
        next_index = (current + index) % len(alphabet)
        answer += alphabet[next_index]
    
    return answer