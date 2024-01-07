def solution(s):
    result = 10 ** 6
    if len(s) == 1:
        return 1

    for period in range(1, len(s)//2 + 1):
        splitted = []
        temp = []
        for i in range(0, len(s), period):
            splitted.append(s[i:i+period])
        start = 0
        while start < len(splitted):
            condition = splitted[start]
            after = start
            while True:
                after += 1
                if after > len(splitted) - 1:
                    after-= 1
                    break
                if splitted[after] == condition:
                    continue
                else:
                    after -= 1
                    break
            temp.append((str(after-start+1)+condition)
                        if not after == start else condition)
            start = after + 1
        result = min(result, len(''.join(temp)))
    return result