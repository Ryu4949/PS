from collections import defaultdict, deque

def count_different(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt += 1
    return cnt


def bfs(begin, visited, graph):
    queue = deque()
    queue.append(begin)
    visited[begin] = 1

    while queue:
        word = queue.popleft()

        for i in graph[word]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[word] + 1

def solution(begin, target, words):
    words.append(begin)

    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if count_different(words[i], words[j]) == 1:
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])

    bfs(begin, visited, graph)

    if not visited[target]:
        return 0
    else:
        return visited[target] - 1

graph = defaultdict(list)
visited = defaultdict(int)

begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log']

print(solution(begin, target, words))
