def check_bracket(array):
    brc_list = []
    for i in array:
        if i == '(' or i == '[':
            brc_list.append(i)
        elif i == ')':
            if len(brc_list) == 0 or brc_list[-1] != '(':
                return 'no'
            else:
                brc_list.pop()
        elif i == ']':
            if len(brc_list) == 0 or brc_list[-1] != '[':
                return 'no'
            else:
                brc_list.pop()

    if len(brc_list) == 0:
        return 'yes'
    else:
        return 'no'

while True:
    data = input()
    if data == '.':
        break

    print(check_bracket(data))



