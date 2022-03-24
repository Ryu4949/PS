import sys
sys.stdin = open('sample_input (24).txt')

hex_to_bi = {'0': '0000', '1': '0001', '2':'0010', '3': '0011', '4':'0100', '5':'0101',
             '6': '0110', '7': '0111', '8': '1000', '9':'1001', 'A':'1010', 'B':'1011',
             'C':'1100','D':'1101', 'E':'1110', 'F':'1111'}
code_key = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2):2, (4, 1, 1):3, (1, 3, 2):4, (2, 3, 1):5, (1, 1, 4):6, (3, 1, 2):7, (2, 1, 3):8, (1, 1, 2):9}

def verify(pw):
    ver = 0

    for i in range(8):
        if i % 2 == 1:
            ver += pw[i] * 3
        else:
            ver += pw[i]

    if ver % 10 == 0:
        return True
    else: return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = list(set([input() for _ in range(N)]))

    for i in range(len(code)):
        bi = ''
        for j in code[i]:
            bi += hex_to_bi[j]
        code[i] = bi.rstrip('0')

    ans = 0
    checked = []
    dec = []
    for i in range(len(code)):
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        for j in range(len(code[i])-1, -1, -1):
            if code[i][j] == '1' and c3 == 0:
                c4 += 1
            elif code[i][j] == '0' and c2 == 0:
                c3 += 1
            elif code[i][j] == '1' and c1 == 0:
                c2 += 1
            elif code[i][j] == '0':
                if code[i][j-1] == '1':
                    r = min(c2, c3, c4)
                    cd = code_key[(c2//r, c3//r, c4//r)]
                    dec.append(cd)
                    c2 = 0
                    c3 = 0
                    c4 = 0
                    if len(dec) == 8:
                        if verify(dec) and dec not in checked:
                            ans += sum(dec)
                            checked.append(dec)
                        dec = []

    print(f'#{tc} {ans}')