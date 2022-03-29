#플레이어별로 몇번째 카드를 가져갔을 때 babygin이 되는지 반환하는 함수
def is_babygin(arr):
    card = [0] * 10
    for i in range(6):
        #i번째 카드를 확인했을 때 해당 카드가 3장이 된다면 i 반환
        card[arr[i]] += 1
        if card[arr[i]] == 3:
            return i

        #i번째 카드 가져간 이후에 연속된 3개 수에 해당하는 카드가 있는지 확인
        #있으면 i 반환
        for j in range(8):
            if card[j] * card[j + 1] * card[j + 2] > 0:
                return i

    #babygin이 불가능한 경우 7 반환
    return 7

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player_1 = [cards[i] for i in range(0, 12, 2)]
    player_2 = [cards[i] for i in range(1, 12, 2)]

    #두 플레이어 모두 babygin 불가능하면 0
    #플레이어 1이 먼저 시작하기 때문에 1의 함수값이 2 이하이면 1의 승리
    #아니면 2의 승리
    if is_babygin(player_1) == 7 and is_babygin(player_2) == 7:
        print(f'#{tc} 0')
    elif is_babygin(player_1) <= is_babygin(player_2):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 2')