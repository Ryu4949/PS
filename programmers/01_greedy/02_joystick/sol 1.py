def solution(name):
    answer = 0
    for i in name:
        answer += min(ord(i)-ord('A'), 26-ord(i)+ord('A'))

    idx = 0
    max_cnt = 0
    cnt = 0
    consecutive_a = []
    for i in range(1, len(name)):
        if name[i] == 'A':
            cnt += 1
            if i == len(name)-1:
                if cnt > max_cnt:
                    max_cnt = cnt
                    idx = i
        else:
            if cnt > 0:
                if cnt > max_cnt:
                    max_cnt = cnt
                    idx = i-1
                cnt = 0

    left_side = idx-max_cnt
    right_side = len(name)-1-idx

    if left_side < max_cnt or right_side < max_cnt:
        side = 2*min(left_side, right_side)+max(left_side, right_side)
    else:
        side = len(name)-1

    print(f'left: {left_side}, right: {right_side}')
    print(f'max_cnt: {max_cnt}, idx: {idx}')
    return answer

print(solution("BBABAAAABBBAAAABABB"))
print(solution("BAAA"))
print(solution("ABABAAAAABA"))
print(solution("ABAAB"))
print(solution("BBAAABB"))
print(solution("BBBAAAB"))
print(solution("BAABAAABBB"))