def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    match_count = len(set(lottos) & set(win_nums))

    best = min(6, 7 - (match_count + zero_count))
    worst = min(6, 7 - match_count)

    return [best, worst]