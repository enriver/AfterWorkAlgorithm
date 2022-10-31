# 요세푸스 문제 0 - S5

import sys
from collections import deque

def solve_one(N,K):
    arr = [_ for _ in range(1,N+1)] # 값이 들어있는 배열
    removed = list() # 제거되는 인덱스 값을 담는 배열

    idx = -1 # 인덱스와 원소 값의 차이를 메꾸기 위한 초기값

    print('<',end='')
    while True: 
        cnt=0 # 이동하는 횟수 count

        while cnt!=K:
            idx+=1

            if idx>=N: # 인덱스 값이 N보다 클 때
                idx-=N
            if idx not in removed:
                cnt+=1

        removed.append(idx)

        if len(removed)==N:
            print(arr[idx],end='')
            break
        print(arr[idx],end=', ')

    print('>')

def solve_two(N,K):
    cnt = 0
    queue = deque()
    ans = ""
    for i in range(1,N+1):
        queue.append(i)
    while queue:
        cnt += 1
        if K == cnt:
            ans = ans + ", " + str(queue.popleft())
            cnt = 0
        else:
            queue.append(queue.popleft())

    ans = ans[2:]
    print("<",end="")
    print(ans,end="")
    print(">",end="")

if __name__ =="__main__":
    n,k = map(int, sys.stdin.readline().split())

    #solve_one(n,k)
    solve_two(n,k)
    