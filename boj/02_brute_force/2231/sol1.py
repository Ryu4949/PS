n = int(input())


def part_sum(num):
    ps = num
    for i in str(num):
        ps += int(i)

    return ps


i = 1
while True:
    if n == part_sum(i):
        print(i)
        break
    i += 1