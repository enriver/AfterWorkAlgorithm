# 과제 안 내신 분..? - B5

import sys

student_list = [x for x in range(1,31)]

for _ in range(28):
    n = int(sys.stdin.readline())
    
    student_list.remove(n)
    
print(student_list[0])
print(student_list[1])