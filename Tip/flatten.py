#2차원 리스트를 1차원 리스트로 만들 때
a = [[1, 2], [3, 4], [5, 6]]

#반복문이나 extend 등을 쓸 수도 있고
b = sum(a, [])

#위와 같이 해줄 수도 있다.
#다만 리스트의 규모가 크다면 시간이 오래걸리므로
#알고리즘 문제를 풀 때는 적합하지 않을 수도 있다.