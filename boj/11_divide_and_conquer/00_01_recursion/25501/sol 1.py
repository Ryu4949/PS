def recursion(s, l, r, n):
    global call
    if l >= r:
        call = n
        return 1
    elif s[l] != s[r]:
        call = n
        return 0
    else:
        return recursion(s, l+1, r-1, n+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

T = int(input())
for _ in range(T):
    call = 0
    word = input()
    print(isPalindrome(word), call)