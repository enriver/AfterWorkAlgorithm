# 촌수계산 - S2

import sys
from collections import defaultdict, deque

def bfs(start, end):
    global children
    global parents
    global visit

    que=deque()
    que.append((start,0))

    while que:
        person, cnt = que.popleft()

        # 찾고자 하는 사람이 있는 경우
        if person==end:
            return cnt
        
        # 부모쪽으로 관계 탐색
        for parent in parents[person]:
            if not visit[parent]:
                visit[parent]=True
                que.append((parent,cnt+1))

        # 자녀쪽으로 관계 탐색
        for child in children[person]:
            if not visit[child]:
                visit[child]=True
                que.append((child,cnt+1))
                
    return -1


if __name__=="__main__":
    n = int(sys.stdin.readline())
    p1, p2 = map(int,sys.stdin.readline().split())

    m = int(sys.stdin.readline())

    children=defaultdict(list)
    parents=defaultdict(list)
    for _ in range(m):
        x,y = map(int,sys.stdin.readline().split())

        children[x].append(y)  # x의 자식은 y이다
        parents[y].append(x) # y의 부모는 x이다

    visit=[False for _ in range(n+1)]
    visit[p1]=True

    # 부모 or 자식 둘다 없으면 관계 성립이 불가하므로 -1
    if len(parents[p1])==0 and len(children[p1])==0:
        print(-1)
    else:
        print(bfs(p1,p2))