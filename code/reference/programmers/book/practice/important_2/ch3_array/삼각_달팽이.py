def solution(n):
    res = [[0] * n for _ in range(n)]   # 모두 0으로 개수만큼 세팅
    answer = []
    x, y = -1, 0        # for문 실행시 x값을 처음에 0으로 세팅해주기 위해 초기값은 -1로 세팅
    num = 1             # 들어갈 숫자

    for i in range(n):
        for j in range(i, n):
            # down
            if i % 3 == 0:          # 3으로 퍼센트연산해준 이유는 down/right/up 세 동작이기 때문
                x += 1

            # right
            elif i % 3 == 1:
                y += 1

            # up
            elif i % 3 == 2:
                x -= 1
                y -= 1

            res[x][y] = num        # res에 저장
            num += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)   # 저장했던 배열 for문이용 합쳐줍니다.

    return answer

'''
1. 문제요약
    - 파라미터
        수 n이 매개변수로 주어짐.
        밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기 진행
    - 그림
        그림으로 로직 이해하라고 함
2. 풀이
    1. 초기화
        - res
            삼각 달팽이를 저장할 res 초기화
        - res에 접근하기 위한 index
            - res의 인덱스에 접근하기 위한 x, y 값을 각각 -1, 0으로 초기화
                - x를 -1로 초기화하는 이유는 for문 사용 시 초기에 x값을 0으로 시작하기 위함
        - num
            - res에 저장할 수 num을 선언 및 초기화
    2. 이중 for문 작성
        - 0~n까지, i~n 까지의 이중 for문을 작성
            -n이 4일 경우
                - 이중 for문으로 한 변을 지날 때마다 4개 -> 3개 -> 2개 -> 1개로 저장할 수 감소
            -i를 % 연산자로 구분
                - i%3==0이면, down
                - i%3==1이면, right
                - i%3==2이면, up
            - num 저장
                - 1씩 증가
                    알맞은 인덱스에 num을 1씩 늘리며 저장
    3.  정답 도출
        - 이중 for문으로 answer에 기존의 2차원 리스트를 하나로 합쳐주자.

[참고]
https://chiefcoder.tistory.com/30
https://programmers.co.kr/learn/courses/30/lessons/68645


'''