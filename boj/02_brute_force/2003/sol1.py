#시간초과로 실패
#리스트 슬라이싱은 은근히 시간이 오래걸리므로 많이 쓰는 건 좋지 않다
#보통 제한시간 1초가 주어질 때가 많은데 보통 1초 = 2000만번을 염두에두고
#시간복잡도를 신경쓰도록 한다.

n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i+1, n+1):
        a = nums[i:j]
        #nums의 값들은 모두 자연수이므로 일단 합이 m이 되면 그 뒤로는 검토 x
        if sum(a) == m:
            cnt += 1
            break

print(cnt)