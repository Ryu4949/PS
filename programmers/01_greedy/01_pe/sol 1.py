def solution(n, lost, reserve):
    answer = 0
    clothes = [1] * n
    for i in lost:
        clothes[i-1] -= 1

    for i in reserve:
        clothes[i-1] += 1

    for i in range(n):
        if i-1 >= 0 and clothes[i] == 2 and clothes[i-1] == 0:
            clothes[i] -= 1
            clothes[i-1] += 1
        elif i+1 < n and clothes[i] == 2 and clothes[i+1] == 0:
            clothes[i] -= 1
            clothes[i+1] += 1

    for i in range(n):
        if clothes[i] > 0:
            answer += 1
    return answer