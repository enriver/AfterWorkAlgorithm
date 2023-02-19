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

        for n in tree[node]:
            if parents[n]==0 and n!=1:
                parents[n]=node
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