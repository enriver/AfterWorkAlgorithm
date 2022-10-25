# ACM 호텔 - B2

import sys

if __name__=="__main__":
    T = int(sys.stdin.readline()) # 테스트케이스 수

    for _ in range(T):
        # H:층 , W:방 , N:몇번째 손님
        H,W,N = map(int, sys.stdin.readline().split())

        floor = 0
        room = 0
        cnt = 0
        
        for i in range(1,W+1):
            if cnt==N:
                break
            room = i

            for j in range(1,H+1):
                floor = j
                cnt+=1

                if cnt==N:
                    break

        if room < 10 :
            print(str(floor)+'0'+str(room))
        else:
            print(str(floor)+str(room))
