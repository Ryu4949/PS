from collections import defaultdict

def solution(n, lost, reserve):
    answer = 0
    uniforms = defaultdict(int)
    for i in range(1, n+1):
        uniforms[i] += 1

    for i in lost:
        uniforms[i] -= 1

    for i in reserve:
        uniforms[i] += 1

    for i in range(1, n+1):
        if uniforms[i] >= 2:
            if i >= 2 and uniforms[i-1] == 0:
                uniforms[i] -= 1
                uniforms[i-1] += 1
            elif i <= n-1 and uniforms[i+1] == 0:
                uniforms[i] -= 1
                uniforms[i+1] += 1

    for i in range(1, n+1):
        if uniforms[i] >= 1:
            answer += 1

    return answer