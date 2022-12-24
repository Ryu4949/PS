def akaraka(word):
    global is_palindrome

    if word != word[::-1]:
        is_palindrome = False
        return

    if len(word) == 1:
        return

    N = len(word)
    half = N // 2

    akaraka(word[:half])
    if N%2:
        akaraka(word[half+1:])
    else:
        akaraka(word[half:])

word = input()
is_palindrome = True
answer = ["IPSELENTI", "AKARAKA"]

akaraka(word)

print(answer[is_palindrome])