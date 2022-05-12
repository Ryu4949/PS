from collections import defaultdict

def solution(N, number):
    num_list = defaultdict(set)
    num_list[1] = {N}

    for i in range(2, 9):
        num_list[i].add(int(str(N) * i))

    for i in range(1, 8):
        for j in range(1, 8):
            if i + j > 8:
                continue

            for k in num_list[i]:
                for l in num_list[j]:
                    num_list[i+j].add(k+l)
                    num_list[i+j].add(abs(k-l))
                    num_list[i+j].add(k*l)
                    if l != 0:
                        num_list[i+j].add(k//l)

    for i in range(1, 9):
        if number in num_list[i]:
            return i
    return -1

'''
정확성  테스트
테스트 1 〉	통과 (15.77ms, 11.1MB)
테스트 2 〉	통과 (1.35ms, 10.3MB)
테스트 3 〉	통과 (3.26ms, 10.4MB)
테스트 4 〉	통과 (9.82ms, 11MB)
테스트 5 〉	통과 (7.04ms, 10.4MB)
테스트 6 〉	통과 (6.72ms, 10.4MB)
테스트 7 〉	통과 (7.98ms, 10.4MB)
테스트 8 〉	통과 (9.52ms, 10.9MB)
테스트 9 〉	통과 (10.06ms, 10.4MB)
'''