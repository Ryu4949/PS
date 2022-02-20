def check_bracket(array):
    n = len(array)
    brc = {'(': 0, ')': 0}
    brc_list = list(array)

    for i in range(n):
        v = brc_list.pop()
        brc[v] += 1
        if brc[')'] < brc['(']:
            return "NO"

    if brc['('] != brc[')']:
        return "NO"
    else:
        return "YES"

T = int(input())
for _ in range(T):
    bracket = list(input())
    print(check_bracket(bracket))