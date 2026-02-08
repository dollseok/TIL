s = input()

buf = []
collecting = False
wbuf = []  # 최근 문자로 "What is" 감지용

for ch in s:
    # 최근 7글자(=len("What is")) 유지
    wbuf.append(ch)
    if len(wbuf) > 7:
        wbuf.pop(0)
    tail = ''.join(wbuf)

    # "What is"를 발견하면: 새 질문 시작(기존 버퍼는 버림)
    if tail == "What is":
        collecting = True
        buf = list("What is")
        continue

    if not collecting:
        continue

    # 질문 수집 중이면, '?'까지 버퍼에 쌓기
    if ch == '?':
        sentence = ''.join(buf).strip()      # buf에는 '?' 없음
        # sentence는 항상 "What is"로 시작
        print("Forty-two" + sentence[4:] + ".")
        collecting = False
        buf = []
        wbuf = []  # 다음 질문 감지를 깔끔하게
    else:
        buf.append(ch)
