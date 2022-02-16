a = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
a_dict = {}
for idx, value in enumerate(a):
    a_dict[value] = idx

n = int(input())
for num in range(1, n + 1):
    a = input()
    cnt = [0] * 10
    num_list = list(input().split())

    # 주어진 데이터를 하나씩 활용하여, 그 값을 key로 갖는 value를 인덱스로 하는 요소의 값을 1씩 증가
    for i in num_list:
        cnt[a_dict[i]] += 1

    print(f'#{num}')
    for i in a_dict.keys():
        print((i + ' ') * cnt[a_dict[i]])