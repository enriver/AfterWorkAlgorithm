# 큐 - S4

import sys

if __name__=="__main__":
    que = list()
    N = int(sys.stdin.readline()) # 명령의 수
    
    for _ in range(N):
        args = list(sys.stdin.readline().split())
        arg = args[0]
        size = len(que)

        if arg == 'push':
            que.append(args[1])
        elif arg == 'pop':
            if size == 0:
                print(-1)
            else :
                print(que[0])
                que.remove(que[0])
        elif arg == 'size':
            print(size)
        elif arg == 'empty':
            if size == 0 :
                print(1)
            else:
                print(0)
        elif arg == 'front':
            if size == 0:
                print(-1)
            else:
                print(que[0])
        elif arg == 'back':
            if size == 0:
                print(-1)
            else:
                print(que[-1])
        else:
            pass