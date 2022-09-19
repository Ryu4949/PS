def is_palinderome(string):
    s = 0
    e = len(string) - 1
    if string == string[::-1]:
        return 0

    while s < e:
        if string[s] == string[e]:
            s += 1
            e -= 1
        else:
            if string[s:e] == string[s:e][::-1]:
                return 1
            elif string[s + 1:e + 1] == string[s + 1:e + 1][::-1]:
                return 1
            else:
                return 2

N = int(input())
for _ in range(N):
    string = input()
    print(is_palinderome(string))