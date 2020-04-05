def main():
    res = ""
    instr = input()
    i=0
    curdepth = 0
    while i < len(instr):
        diff = int(instr[i]) - curdepth
        if diff > 0:
            res += diff*'('+instr[i]
            curdepth += diff
            i += 1
        elif diff == 0:
            res += instr[i]
            i += 1
        elif diff < 0:
            # import pdb; pdb.set_trace()
            res += abs(diff)*')'+instr[i]
            curdepth += diff
            i += 1
        else:
            raise ValueError('A very specific bad thing happened.')
        # if instr[i] == "0":
        #     res += "0"
        #     i += 1
        # elif instr[i] == "1":
        #     res += "(1"
        #     i += 1
        #     # import pdb; pdb.set_trace()
        #     while i < len(instr) and instr[i] == "1":
        #         res += "1"
        #         i += 1
        #     res += ")"
        # else:
        #     i+=1
    res += curdepth*')'

    print("Case #{}: {}".format(casenum, res))


t = int(input())
casenum = 1

while casenum<=t:
    main()
    casenum += 1

#test
'''
1
101

(1)0(1)

0111
0(111)
0(111)0
0(111)000
'''