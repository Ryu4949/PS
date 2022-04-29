def solution(number, k):
    answer = []
    N = len(number)

    i = 0
    cnt = 0
    while i < N:
        if cnt == k:
            answer.append(number[i])
            i += 1
        else:
            if not answer:
                answer.append(number[i])
                i += 1
            else:
                if number[i] > answer[-1]:
                    answer.pop()
                    cnt += 1
                else:
                    answer.append(number[i])
                    i += 1

    if cnt == k:
        return ''.join(answer)
    else:
        return ''.join(answer[:N - (k - cnt)])