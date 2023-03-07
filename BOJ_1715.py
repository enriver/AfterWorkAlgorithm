# 카드 정렬하기 - G4

import sys
from queue import PriorityQueue

def solve(que):
    result=0

    while True:
        if que.qsize() ==1: # 큐의 크기가 1이면 더이상 비교할 값이 없음
            break

        # 최소값 2개를 가져와서 더함
        q1=que.get()
        q2=que.get()
        newQ=q1+q2

        result+=newQ # 누적합
        que.put(newQ) # 더한 값을 다시 큐에 넣어줌

    return result


if __name__=="__main__":
    N = int(sys.stdin.readline())

    cards = PriorityQueue() # 우선순위 큐 선언
    for _ in range(N):
        cards.put(int(sys.stdin.readline()))

    if N == 1: # 1번의 입력만 있는 경우
        print(0) # 비교할 필요가 없으므로 0 출력
    else:
        print(solve(cards))