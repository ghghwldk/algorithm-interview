from itertools import combinations

def calculation(eq1, eq2):
    x1, y1, c1 = eq1 # 직선1
    x2, y2, c2 = eq2 # 직선2

    # 기울기가 깉아 해가 없는 경우
    if x1*y2 == y1*x2:
        return

    # 두 직선의 해
    x = (y1*c2-c1*y2)/(x1*y2-y1*x2)
    y = (c1*x2-x1*c2)/(x1*y2-y1*x2)

    # 두 직선의 해 x, y가 모두 정수라면 반환
    if x == int(x) and y == int(y):
        return [int(x), int(y)]

def solution(lines):
    points = []
    # 모든 선들의 교점 확인
    for eq1, eq2 in combinations(lines,2):
        point = calculation(eq1,eq2)
        if point: points.append(point)

    # 그림의 시작점과 마지막점 찾기
    w1, w2 = min(points, key = lambda x : x[0])[0], max(points, key = lambda x : x[0])[0] + 1
    h1, h2 = min(points, key = lambda x : x[1])[1], max(points, key = lambda x : x[1])[1] + 1

    # 별을 포함하는 최소한의 크기 배열 생성
    answer = [['.'] * (w2 - w1) for _ in range((h2 - h1))]

    # 그림의 시작점을 기준으로 교점 위치 "*" 변환
    for x, y in points:
        answer[y-h1][x-w1] = '*'

    answer.reverse()

    return [''.join(a) for a in answer]

'''
1. 문제요약
    - n개의 직선 제공
        Ax + By + C = 0으로 표현할 수 있는 n개의 직선 제공
    - 교점조건
        정수로 표현되는 좌표가 교점
    - 정답표현
        격자판은 무한히 넓으니 모든 별을 포함하는 최소한의 크기를 정답으로 표현

2. calculation 함수
    - 정의
        두 직선의 교점의 값을 반환해 주는 함수
    - 조건
        - 무효조건
            만약 두 직선의 기울기가 같다면 함수를 종료
        - 유효조건
            만약 교점인 x, y 모두가 정수라면 교점 값을 반환

3. calculation 함수 활용
    1. 조합 생성
        combinations() 함수를 통해 직선을 만들 수 있는 모든 조합 생성
    2. calculation 함수 실행
        1. 생성된 조합을 기반으로 calculation 함수를 실행
        2. calculation() 함수의 결괏값을 points 배열에 저장

4. 정답 도출
    1. points 배열의 x값 기준 최댓값과 최솟값, y 값 기준 최댓값과 최솟값을 w1, w2, h1, h2 변수에 저장
    2. w1, w2, h1, h2를 활용하여 최소크기의 격자판(answer)를 생성

5. 참고
https://programmers.co.kr/learn/courses/30/lessons/81302
https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Programmers-%EA%B5%90%EC%A0%90%EC%97%90-%EB%B3%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python
'''