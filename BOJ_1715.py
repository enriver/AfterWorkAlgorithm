# 카드 정렬하기 - G4

import sys
from queue import PriorityQueue

def solve(que):
    result=0

    while True:
        if que.qsize() ==1:
            break

        q1=que.get()
        q2=que.get()

        newQ=q1+q2
        result+=newQ
        que.put(newQ)

    return result


if __name__=="__main__":
    N = int(sys.stdin.readline())

    cards = PriorityQueue()
    for _ in range(N):
        cards.put(int(sys.stdin.readline()))

    if N == 1:
        print(0)
    else:
        print(solve(cards))