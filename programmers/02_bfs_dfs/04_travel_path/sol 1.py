from collections import defaultdict


def find_path(airports, v, visited, path, answer):
    if len(path) == len(visited) + 1:
        answer.append(path)
        return

    for i in airports[v[0]]:
        if not visited[i[1]]:
            visited[i[1]] = True
            find_path(airports, i, visited, path + [i[0]], answer)
            visited[i[1]] = False


def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: x[1])
    airports = defaultdict(list)
    visited = [False] * len(tickets)

    for i in range(len(tickets)):
        airports[tickets[i][0]].append((tickets[i][1], i))

    for i in airports["ICN"]:
        visited[i[1]] = True
        find_path(airports, i, visited, ["ICN", i[0]], answer)
        visited[i[1]] = False

        if answer:
            break

    return answer[0]