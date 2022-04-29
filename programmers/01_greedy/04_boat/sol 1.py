def solution(people, limit):
    answer = 0
    people.sort()

    start = 0
    end = len(people) - 1

    while start < end:
        if people[start] + people[end] > limit:
            answer += 1
            end -= 1
        else:
            answer += 1
            start += 1
            end -= 1

    if start == end:    #마지막에 두 포인터가 같아지면 한명 더 있는거니까 한대 더필요
        return answer + 1
    else:   #포인터가 엇갈렸다면 남은 사람이 없는 경우니까 그대로 answer 반환
        return answer
