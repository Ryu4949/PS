S = input()
T = input()
N = len(S)
answer = 0

def s_to_t(s, t):
    global answer

    if len(t) == N and t == s:
        answer = 1
        return

    if len(t) == N:
        return

    if t[-1] == "A":
        s_to_t(s, t[:-1])

    if t[0] == "B":
        s_to_t(s, t[::-1][:-1])

s_to_t(S, T)
print(answer)