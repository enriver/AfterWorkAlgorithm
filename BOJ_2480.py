# 주사위 세개 - B4

import sys


if __name__ == "__main__":
    dices = list(map(int,sys.stdin.readline().split()))

    count_dice =dict()

    for dice in dices:
        if dice not in count_dice.keys():
            count_dice[dice] = 1
        else:
            count_dice[dice] +=1

    # 빈도수가 높은 순으로 우선 정렬, 이후에는 주사위 눈금 값을 기준으로 정렬
    count_dice = sorted(count_dice.items(), key = lambda x:(x[1],x[0]), reverse=True)
    
    # 제일 많이 등장한 주사위
    frq_dice = count_dice[0]

    if frq_dice[1] == 3: # 빈도수가 3이라면
        print(10000 + frq_dice[0]*1000)
    elif frq_dice[1] == 2: # 빈도수가 2라면
        print(1000 + frq_dice[0]*100)
    else:
        print(frq_dice[0]*100)
