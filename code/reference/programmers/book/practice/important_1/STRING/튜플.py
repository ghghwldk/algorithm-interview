'''
성질(중복, 순서, 개수)

중복되는 원소가 없는 튜플이 주어짐
'''
from collections import Counter
def solution(s):
    result = []

    s= s[2:-2]
    elements = s.split('},{')
    elements = sorted(elements, key = lambda x: len(x))
    # counter에는 길이 순서대로 삽입
    counters = []
    for e in elements:
        atoms = e.split(',')
        counters.append(Counter(atoms))

    for i, c in enumerate(counters):
        if i == 0:
            append(result, c)
        else:
            beforeC = counters[i-1]
            diff = c - beforeC
            append(result, diff)
    return result

def append(result, c):
    result.append(int(list(c.keys())[0]))