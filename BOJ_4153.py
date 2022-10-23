# 직각삼각형 - B3

import sys

if __name__=="__main__":
    
    while True:
        sides = sorted(list(map(int,sys.stdin.readline().split())))

        if sides[0]==0:
            break
        
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            print('right')
        else:
            print('wrong')