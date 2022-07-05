new_id = input()
new_id = new_id.lower()

new_recommend = ''

for i in new_id:
    if i.isalnum() or i == '-' or i == '_':
        new_recommend += i
    elif i == '.':
        if not new_recommend:
            new_recommend += i
        elif new_recommend[-1] != '.':
            new_recommend += i

new_recommend = new_recommend.strip('.')

if not new_recommend:
    new_recommend += 'a'

if len(new_recommend) >= 16:
    new_recommend = new_recommend[:15].rstrip('.')

if len(new_recommend) <= 2:
    new_recommend += new_recommend[-1] * (3-len(new_recommend))

print(new_recommend)