def solution(brown, yellow):
    # 세로를 기준으로 while문을 돌리겠다는 이야기이다.
    가, 세 = -1, 3 # 가는 아직 설정 전, 세는 최소 3
    while True:
        if not yellow % (세-2) == 0:
            세 += 1
            continue
        가 = yellow // (세-2) + 2
        브 = 가 * 세 - yellow
        if 브 == brown:
            break
        else:
            세 += 1
    return [가, 세]