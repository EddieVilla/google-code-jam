def main():
    inarr = input().split(' ')
    n = int(inarr[0])
    trace = int(inarr[1])
    if n>5:
        pass # TODO second part goes here
    elif n==2:
        if trace==2:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("1 2")
            print("2 1")
        elif trace==4:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("2 1")
            print("1 2")
        else:
            print("Case #{}: {}".format(casenum, "IMPOSSIBLE"))
    elif n==3:
        if trace==3:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("1 2 3")
            print("3 1 2")
            print("2 3 1")
        elif trace==6:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("2 1 3")
            print("3 2 1")
            print("1 3 2")
        elif trace==9:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("3 2 1")
            print("1 3 2")
            print("2 1 3")
        else:
            print("Case #{}: {}".format(casenum, "IMPOSSIBLE"))
    elif n==4:
        if trace==4:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("1 2 3 4")
            print("2 1 4 3")
            print("3 4 1 2")
            print("4 3 2 1")
        elif trace==6:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("1 3 4 2")
            print("3 2 1 4")
            print("4 1 2 3")
            print("2 4 3 1")
        elif trace==7:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("3 4 2 1")
            print("2 1 3 4")
            print("4 2 1 3")
            print("1 3 4 2")
        elif trace==8:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("1 2 4 3")
            print("2 3 1 4")
            print("4 1 3 2")
            print("3 4 2 1")
        elif trace==9:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 3 2 1")
            print("2 1 3 4")
            print("3 4 1 2")
            print("1 2 4 3")
        elif trace==10:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("2 1 4 3")
            print("1 3 2 4")
            print("4 2 3 1")
            print("3 4 1 2")
        elif trace==11:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 3 2 1")
            print("3 1 4 2")
            print("1 2 3 4")
            print("2 4 1 3")
        elif trace==12:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 1 3 2")
            print("1 2 4 3")
            print("3 4 2 1")
            print("2 3 1 4")
        elif trace==13:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 3 2 1")
            print("2 4 1 3")
            print("1 2 3 4")
            print("3 1 4 2")
        elif trace==14:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 1 2 3")
            print("1 3 4 2")
            print("2 4 3 1")
            print("3 2 1 4")
        elif trace==16:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 2 3 1")
            print("2 4 1 3")
            print("3 1 4 2")
            print("1 3 2 4")
        else:
            print("Case #{}: {}".format(casenum, "IMPOSSIBLE"))
    elif n==5:
        if trace==5:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("1 2 3 4 5")
            print("5 1 2 3 4")
            print("4 5 1 2 3")
            print("3 4 5 1 2")
            print("2 3 4 5 1")
        elif trace==6:
            print("Case #{}: {}".format(casenum, "IMPOSSIBLE"))
        elif trace==7:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("1 3 5 2 4")
            print("2 1 4 5 3")
            print("5 4 2 3 1")
            print("4 2 3 1 5")
            print("3 5 1 4 2")
        elif trace==8:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("3 4 2 1 5")
            print("4 1 3 5 2")
            print("2 5 1 4 3")
            print("1 3 5 2 4")
            print("5 2 4 3 1")
        elif trace==9:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("2 3 1 4 5")
            print("3 1 5 2 4")
            print("4 2 3 5 1")
            print("5 4 2 1 3")
            print("1 5 4 3 2")
        elif trace==10:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("2 4 1 3 5")
            print("4 1 5 2 3")
            print("3 2 4 5 1")
            print("5 3 2 1 4")
            print("1 5 3 4 2")
        elif trace==11:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("2 5 1 3 4")
            print("5 1 4 2 3")
            print("3 2 5 4 1")
            print("4 3 2 1 5")
            print("1 4 3 5 2")
        elif trace==12:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("1 4 3 2 5")
            print("4 3 5 1 2")
            print("2 1 4 5 3")
            print("5 2 1 3 4")
            print("3 5 2 4 1")
        elif trace==13:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 1 2 3 5")
            print("1 2 5 4 3")
            print("3 4 1 5 2")
            print("5 3 4 2 1")
            print("2 5 3 1 4")
        elif trace==14:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("3 4 2 1 5")
            print("4 2 5 3 1")
            print("1 3 4 5 2")
            print("5 1 3 2 4")
            print("2 5 1 4 3")
        elif trace==15:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("3 5 2 1 4")
            print("5 2 4 3 1")
            print("1 3 5 4 2")
            print("4 1 3 2 5")
            print("2 4 1 5 3")
        elif trace==16:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 2 3 1 5")
            print("2 3 5 4 1")
            print("1 4 2 5 3")
            print("5 1 4 3 2")
            print("3 5 1 2 4")
        elif trace==17:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 5 2 1 3")
            print("5 2 3 4 1")
            print("1 4 5 3 2")
            print("3 1 4 2 5")
            print("2 3 1 5 4")
        elif trace==18:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("5 4 2 1 3")
            print("4 2 3 5 1")
            print("1 5 4 3 2")
            print("3 1 5 2 4")
            print("2 3 1 4 5")
        elif trace==19:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 5 3 1 2")
            print("5 3 2 4 1")
            print("1 4 5 2 3")
            print("2 1 4 3 5")
            print("3 2 1 5 4")
        elif trace==20:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("5 4 3 1 2")
            print("4 3 2 5 1")
            print("1 5 4 2 3")
            print("2 1 5 3 4")
            print("3 2 1 4 5")
        elif trace==21:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("4 3 5 1 2")
            print("3 5 2 4 1")
            print("1 4 3 2 5")
            print("2 1 4 5 3")
            print("5 2 1 3 4")
        elif trace==22:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("3 2 4 5 1")
            print("2 5 3 1 4")
            print("4 1 5 2 3")
            print("5 3 1 4 2")
            print("1 4 2 3 5")
        elif trace==23:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("5 3 1 4 2")
            print("4 5 2 1 3")
            print("1 2 4 3 5")
            print("2 4 3 5 1")
            print("3 1 5 2 4")
        elif trace==24:
            print("Case #{}: {}".format(casenum, "IMPOSSIBLE"))
        elif trace==25:
            print("Case #{}: {}".format(casenum, "POSSIBLE"))
            print("5 4 3 2 1")
            print("1 5 4 3 2")
            print("2 1 5 4 3")
            print("3 2 1 5 4")
            print("4 3 2 1 5")
        else:
            print("Case #{}: {}".format(casenum, "IMPOSSIBLE"))
    else:
        raise ValueError('UNEXPECTED ELSE')


t = int(input())
casenum = 1

while casenum<=t:
    main()
    casenum += 1

#test
'''

'''