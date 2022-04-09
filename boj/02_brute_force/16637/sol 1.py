def sub(str):
    result = 0
    i = 0
    while True:
        if str[i] in '+-*':
            if str[i] == '+':
                result += int(str[i+1])
                i += 2
            elif str[i] == '-':
                result -= int(str[i+1])
                i += 2
            else:
                result *= int(str[i+1])
                i += 2
        else:
            result += int(str[i])
            i += 1
        if i == len(str):
            return result

def cal(i, exp):
    if i >= N:
        rlt.append(sub(exp))
        return

    if sentence[i].isdigit() and i>=N-2:
        cal(i+1, exp+[sentence[i]])
    elif sentence[i].isdigit() and i<=N-3:
        cal(i + 1, exp + [sentence[i]])
        cal(i+3, exp+[str(sub(sentence[i]+sentence[i+1]+sentence[i+2]))])
    else:
        cal(i+1, exp+[sentence[i]])

N = int(input())
sentence = list(input())
rlt = []

cal(0, [])

print(max(rlt))