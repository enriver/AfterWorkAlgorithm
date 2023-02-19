# 트리의 부모 찾기 - S2
# https://velog.io/@dardk6ro/ 참고

import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**8)

def solve(tree,N):
    parents=[0 for _ in range(N+1)]

    que=deque()
    que.append(1)

    while que:
        node = que.popleft()

        for n in tree[node]: # 해당 노드의 value를 조회
            if parents[n]==0 and n!=1: # value 값이 1이 아니면서, 방문한 적이 없다면
                parents[n]=node # 해당 value의 부모를 key값으로 정의
                que.append(n)

    for i in range(2,N+1):
        print(parents[i])



if __name__=="__main__":
    N=int(sys.stdin.readline())
    tree=defaultdict(list)

    for _ in range(N-1):
        n1, n2 =map(int,sys.stdin.readline().split())
        
        tree[n1].append(n2)
        tree[n2].append(n1)

    solve(tree,N)