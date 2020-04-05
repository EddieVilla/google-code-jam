def main():
    res = ""
    instr = input()
    i=0
    while i < len(instr):
        if instr[i] == "0":
            res += "0"
            i += 1
        elif instr[i] == "1":
            res += "(1"
            i += 1
            # import pdb; pdb.set_trace()
            while i < len(instr) and instr[i] == "1":
                res += "1"
                i += 1
            res += ")"
        else:
            i+=1

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