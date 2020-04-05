import math
t = int(input())
casenum = 1

while casenum<=t:
    main()

def main():
    n = int(input())
    lenn = int(math.log10(n)) + 1
    mask = lenn
    d = n//lenn