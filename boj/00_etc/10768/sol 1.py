M = int(input())
D = int(input())

if M*100+D == 218:
    print("Special")
elif M*100+D > 218:
    print("After")
else:
    print("Before")