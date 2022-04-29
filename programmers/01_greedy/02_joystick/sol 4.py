def solution(name):
    answer = 0
    for i in name:
        answer += min(ord(i)-ord('A'), 26-ord(i)+ord('A'))

    idx = 0
    max_cnt = 0
    cnt = 0

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

    to_left = 0
    for i in range(1, len(name)):
        if name[i] == 'A':
            to_left += 1
        else:
            break

    to_right = 0
    for i in range(len(name)-1, 0, -1):
        if name[i] == 'A':
            to_right += 1
        else:
            break

    left_side = idx-max_cnt
    right_side = len(name)-1-idx

    if left_side < max_cnt or right_side < max_cnt:
        side = 2*min(left_side, right_side)+max(left_side, right_side)
    else:
        side = len(name)-1

    answer += min(side, len(name)-1-to_left, len(name)-1-to_right)
    return answer

print(solution("BBABAAAABBBAAAABABB"))  #26
print(solution("BAAA")) #1
print(solution("ABABAAAAABA"))  #10
print(solution("ABAAB"))    #5
print(solution("BBAAABB"))  #8
print(solution("BBBAAAB"))  #8
print(solution("BAABAAABBB"))   #12
print(solution("BBAAAAABAAAAABB"))
print(solution("BBBAAAAABAAAAAB"))