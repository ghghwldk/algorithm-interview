import sys
def solution(s):
    # sys.setrecursionlimit(10**6)

    if not len(s) % 2 == 0:
        return -1
    removed = s
    isPossible = False
    while True:
        isPossible, removed = remove(removed)
        if len(removed) == 0:
            return 1
        else:
            if not isPossible:
                return 0
    return 0

def remove(s):
    isPossible, removed = False, s
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            removed = s[:i] + s[i+2:]
            isPossible = True
            break
    return isPossible, removed