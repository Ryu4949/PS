def count_blueray(length, array):
    cnt = 1
    lecture = 0
    for i in range(len(array)):
        if lecture + array[i] > length:
            lecture = 0
            lecture += array[i]
            cnt += 1
        else:
            lecture += array[i]
    return cnt


print(count_blueray(15, [1, 2, 3, 4, 5, 6, 9, 8]))