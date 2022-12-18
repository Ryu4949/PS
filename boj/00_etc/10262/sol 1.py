ga1, gb1, ga2, gb2 = map(int, input().split())
ea1, eb1, ea2, eb2 = map(int, input().split())

gunnar = ga1+gb1+ga2+gb2
emma = ea1+eb1+ea2+eb2

if gunnar > emma:
    print("Gunnar")
elif gunnar < emma:
    print("Emma")
else:
    print("Tie")
