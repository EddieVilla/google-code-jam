# import numpy as np

def main():
    n = int(input())
    matR = []
    matC = []
    for _ in range(n):
        instr = input()
        rowstr = instr.split(' ')
        rowint = [int(c) for c in rowstr]
        matR.append(rowint)
    
    trace = 0
    for i in range(len(matR)):
        trace += matR[i][i]
    
    for i in range(len(matR)):
        col = []
        for j in range(len(matR)):
            col.append(matR[j][i])
        matC.append(col)
    
    # print(matR)
    # print(matC)

    rowdups = 0
    coldups = 0
    for i in range(len(matR)):
        rcur = matR[i]
        if len(rcur) != len(set(rcur)):
            rowdups += 1
        ccur = matC[i]
        if len(ccur) != len(set(ccur)):
            coldups += 1

    print("Case #{}: {} {} {}".format(casenum, trace, rowdups, coldups))


t = int(input())
casenum = 1

while casenum<=t:
    main()
    casenum += 1

#test
'''

'''