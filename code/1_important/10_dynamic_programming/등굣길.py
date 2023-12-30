'''
[문제 유형 분석]
dp 문제 >> 점화식 구하기
dp[i][j] = dp[i-1][j] + dp[i][j-1]

[갈 수 없는 길의 표현]
- 0으로 표현
    - 해당 칸으로 가는 경우를 생략하는 방법
[시작 위치 경우의 수 표현]
- 1로 표현
    - 시작 위치로 가는 방법은 반드시 1개 존재
'''
def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles] # 좌표 r, c 변경 >> 평소대로 풀이
    dp = [[0] * (m + 1) for i in range(n + 1)] # dp초기화
    dp[1][1] = 1 # 시작위치 경우의 수 초기화

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue  # 시작점 제외
            if [i, j] in puddles: dp[i][j] = 0 # 웅덩이로 갈 수 없음 >> 경우의 수 0으로 표현
            else: # 현재 칸의 값은 왼쪽 칸, 위 칸의 합산값과 동일
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007 # 매우 큰 값에 대비
    return dp[n][m] # 종착지로 가는 경우의 수 리턴