def solution(name):
    answer = 0
    for i in name:
        answer += min(ord(i)-ord('A'), 26-ord(i)+ord('A'))

    consecutive_a = []
    cnt = 0
    start = 0
    last = None
    for i in range(1, len(name)):
        if name[i] == 'A':
            cnt += 1
            if last != 'A':
                last = 'A'
                start = i

            if i == len(name)-1:
                consecutive_a.append((cnt, start, i))
        else:
            if last == 'A':
                consecutive_a.append((cnt, start, i-1))
                last = name[i]
            cnt = 0

    print(consecutive_a)

    side = len(name)+1
    left = len(name)+1
    right = len(name)+1
    if consecutive_a:
        max_cons = max(consecutive_a, key=lambda x: x[0])
        max_cnt = max_cons[0]
        idx = max_cons[2]

        left_side = idx-max_cnt
        right_side = len(name)-1-idx

        if left_side < max_cnt or right_side < max_cnt:
            side = 2*min(left_side, right_side)+max(left_side, right_side)
        else:
            side = len(name)-1

    for i in consecutive_a:
        if i[1] == 1:
            left = len(name)-1-(i[2]-i[1]+1)
        if i[2] == len(name)-1:
            right = len(name)-1-(i[2]-i[1]+1)
    # print(f'left: {left_side}, right: {right_side}')
    # print(f'max_cnt: {max_cnt}, idx: {idx}')
    return answer+min(side, left, right)

print(solution("BBABAAAABBBAAAABABB"))
print(solution("BAAA"))
print(solution("ABABAAAAABA"))
print(solution("ABAAB"))
print(solution("BBAAABB"))
print(solution("BBBAAAB"))
print(solution("BAABAAABBB"))
print(solution("JEROEN"))