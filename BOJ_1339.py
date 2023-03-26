# 단어 수학 - G4

import sys

def solve(array):
    result = [array[0]+array[1]]
    if len(array)==1:
        return 0
    elif len(array)==2:
        return sum(array)
    else:
        for i in range(2,len(array)):
            val=result[-1]

            if i == len(array)-1:
                result.append(val+array[i])
                break

            if val+array[i] <= array[i+1]:
                result.append(val+array[i])
            else:
                result.append(array[i])

    return result

if __name__=="__main__":
    N = int(sys.stdin.readline())
    cards = list()

    for _ in range(N):
        cards.append(int(sys.stdin.readline()))

    cards.sort()

    print(solve(cards))