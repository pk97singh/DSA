#find longest string without repeated characters.
s = "abcabcbb"

res = 0
char = set()
low = 0
high = 0
n = len(s)

while high < n:

    while s[high] in char:
        char.remove(s[low])
        low = low + 1

    char.add(s[high])

    res = max(res, high - low + 1)

    high = high + 1

print(res)
