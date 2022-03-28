S = input()
check = 'UCPC'

def check_UCPC(string):
    idx = 0

    for i in range(len(string)):
        if string[i] == check[idx]:
            idx += 1
        if idx == 4:
            return True
    return False

if check_UCPC(S):
    print('I love UCPC')
else:
    print('I hate UCPC')