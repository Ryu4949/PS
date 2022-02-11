N=int(input())

numbers=[]
for _ in range(N):
    numbers.append(int(input()))

#for i in range(N-1,0,-1): # 수업시간에 배운대로 i를 하나씩 줄여가면 172ms
#   for j in range(0,i):

for _ in range(N): # 무지성으로 처음부터 끝까지 N번 훑으면 148ms, 이게더빠르네???
    for j in range(N-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

for number in numbers:
    print(number)