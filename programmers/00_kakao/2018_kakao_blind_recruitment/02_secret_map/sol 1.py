def to_binary(n, l):
    return map(int, list(bin(n)[2:].zfill(l)))

def solution(n, arr1, arr2):
    answer = [[0]*n for _ in range(n)]
    map1 = [[*to_binary(arr1[i], n)] for i in range(n)]
    map2 = [[*to_binary(arr2[i], n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            answer[i][j] = "#" if map1[i][j] or map2[i][j] else " "

    answer = list(map(lambda x: ''.join(x), answer))
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))