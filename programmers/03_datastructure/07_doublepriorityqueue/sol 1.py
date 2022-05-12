import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    visited = []
    idx = 0

    for i in operations:
        if i[0] == "I":
            num = int(i[2:])
            heapq.heappush(max_heap, (-num, idx))
            heapq.heappush(min_heap, (num, idx))
            idx += 1
            visited.append(False)
        else:
            if max_heap and len(i) == 3:
                while max_heap:
                    mx = heapq.heappop(max_heap)
                    if not visited[mx[1]]:
                        visited[mx[1]] = True
                        break
            elif min_heap and len(i) == 4:
                while min_heap:
                    mn = heapq.heappop(min_heap)
                    if not visited[mn[1]]:
                        visited[mn[1]] = True
                        break

    max_value = 0
    min_value = 0
    while max_heap:
        a = heapq.heappop(max_heap)
        if visited[a[1]] == False:
            max_value = -a[0]
            break

    while min_heap:
        b = heapq.heappop(min_heap)
        if visited[b[1]] == False:
            min_value = b[0]
            break

    return [max_value, min_value]

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.6MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.5MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.5MB)
'''

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["D 1", "I 7"]))
print(solution(["I 4", "I -1", "I 6", "I 3"]))
print(solution(["D 1", "D -1"]))
print(solution(["I 3", "I 3"]))
print(solution(["I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"]))    #[40, 40]