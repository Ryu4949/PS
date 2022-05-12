from collections import defaultdict

def solution(N, number):
    num_list = defaultdict(set)
    num_list[1] = {N}
    operators = ['+', '-', '*', '//']

    for i in range(2, 9):
        num_list[i].add(int(str(N) * i))

    for i in range(1, 8):
        for j in range(1, 8):
            if i + j > 8:
                continue

            for k in num_list[i]:
                for l in num_list[j]:
                    if l != 0:
                        for op in operators:
                            new_num = abs(eval(str(k) + op + str(l)))
                            num_list[i + j].add(new_num)

    for i in range(1, 9):
        if number in num_list[i]:
            return i
    return -1

'''
정확성  테스트
테스트 1 〉	통과 (327.80ms, 11.1MB)
테스트 2 〉	통과 (43.76ms, 10.5MB)
테스트 3 〉	통과 (116.26ms, 10.4MB)
테스트 4 〉	통과 (477.00ms, 11.2MB)
테스트 5 〉	통과 (255.26ms, 10.5MB)
테스트 6 〉	통과 (235.47ms, 10.5MB)
테스트 7 〉	통과 (277.57ms, 10.8MB)
테스트 8 〉	통과 (399.37ms, 11.1MB)
테스트 9 〉	통과 (199.90ms, 10.4MB)
'''