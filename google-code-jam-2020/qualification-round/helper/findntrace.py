#findntrace
import copy
from itertools import permutations

def helper(alist):
    for itrk in range(len(alist)):
        pickeda = alist[itrk] # 2 picked
        clist = copy.deepcopy(alist)
        clist.remove(pickeda)
        for i in range(len(clist)-1,-1,-1):
            if clist[i][0]==pickeda[0]:
                clist.remove(clist[i])
        for i in range(len(clist)-1,-1,-1):
            if clist[i][1]==pickeda[1]:
                clist.remove(clist[i])
        for i in range(len(clist)-1,-1,-1):
            if clist[i][2]==pickeda[2]:
                clist.remove(clist[i])
        for i in range(len(clist)-1,-1,-1):
            if clist[i][3]==pickeda[3]:
                clist.remove(clist[i])
        for i in range(len(clist)-1,-1,-1):
            if clist[i][4]==pickeda[4]:
                clist.remove(clist[i])
        for itrl in range(len(clist)):
            pickedc = clist[itrl] # 3 picked
            dlist = copy.deepcopy(clist)
            dlist.remove(pickedc)
            for i in range(len(dlist)-1,-1,-1):
                if dlist[i][0]==pickedc[0]:
                    dlist.remove(dlist[i])
            for i in range(len(dlist)-1,-1,-1):
                if dlist[i][1]==pickedc[1]:
                    dlist.remove(dlist[i])
            for i in range(len(dlist)-1,-1,-1):
                if dlist[i][2]==pickedc[2]:
                    dlist.remove(dlist[i])
            for i in range(len(dlist)-1,-1,-1):
                if dlist[i][3]==pickedc[3]:
                    dlist.remove(dlist[i])
            for i in range(len(dlist)-1,-1,-1):
                if dlist[i][4]==pickedc[4]:
                    dlist.remove(dlist[i])
            for itrm in range(len(dlist)):
                pickedd = dlist[itrm] # 4 picked
                elist = copy.deepcopy(dlist)
                elist.remove(pickedd)
                for i in range(len(elist)-1,-1,-1):
                    if elist[i][0]==pickedd[0]:
                        elist.remove(elist[i])
                for i in range(len(elist)-1,-1,-1):
                    if elist[i][1]==pickedd[1]:
                        elist.remove(elist[i])
                for i in range(len(elist)-1,-1,-1):
                    if elist[i][2]==pickedd[2]:
                        elist.remove(elist[i])
                for i in range(len(elist)-1,-1,-1):
                    if elist[i][3]==pickedd[3]:
                        elist.remove(elist[i])
                for i in range(len(elist)-1,-1,-1):
                    if elist[i][4]==pickedd[4]:
                        elist.remove(elist[i])
                return elist[0]
                for itrn in range(len(elist)):
                    pickede = elist[itrn] # 5 picked
                    # print("MY PICK")
                    # print(pickedb)
                    # print(pickeda)
                    # print(pickedc)
                    # print(pickedd)
                    # print(pickede)
                    # print("END")
                    myarr = []
                    myarr.append(pickedb)
                    myarr.append(pickeda)
                    myarr.append(pickedc)
                    myarr.append(pickedd)
                    myarr.append(pickede)
                    # print(myarr)
                    trace0 = myarr[0][0] + myarr[1][1] + myarr[2][2] + myarr[3][3] + myarr[4][4]
                    trace1 = myarr[0][1] + myarr[1][2] + myarr[2][3] + myarr[3][4] + myarr[4][0]
                    trace2 = myarr[0][2] + myarr[1][3] + myarr[2][4] + myarr[3][0] + myarr[4][1]
                    trace3 = myarr[0][3] + myarr[1][4] + myarr[2][0] + myarr[3][1] + myarr[4][2]
                    trace4 = myarr[0][4] + myarr[1][0] + myarr[2][1] + myarr[3][2] + myarr[4][3]
                    trace5 = myarr[4][0] + myarr[3][1] + myarr[2][2] + myarr[1][3] + myarr[0][4]
                    trace6 = myarr[4][1] + myarr[3][2] + myarr[2][3] + myarr[1][4] + myarr[0][0]
                    trace7 = myarr[4][2] + myarr[3][3] + myarr[2][4] + myarr[1][0] + myarr[0][1]
                    trace8 = myarr[4][3] + myarr[3][4] + myarr[2][0] + myarr[1][1] + myarr[0][2]
                    trace9 = myarr[4][4] + myarr[3][0] + myarr[2][1] + myarr[1][2] + myarr[0][3]
                    special = 7
                    if trace0==special:
                        print("trace0")
                        for num1 in range(len(myarr)):
                            for num2 in range(len(myarr[num1])):
                                print(myarr[num1][num2], end= ' ')
                            print()
                        print("--7")
                    elif trace1==special:
                        print("trace1")
                        for num1 in range(len(myarr)):
                            for num2 in range(len(myarr[num1])):
                                print(myarr[num1][num2], end= ' ')
                            print()
                        print("--7")
                    elif trace2==special:
                        print("trace2")
                        for num1 in range(len(myarr)):
                            for num2 in range(len(myarr[num1])):
                                print(myarr[num1][num2], end= ' ')
                            print()
                        print("--7")
                    elif trace3==special:
                        print("trace3")
                        for num1 in range(len(myarr)):
                            for num2 in range(len(myarr[num1])):
                                print(myarr[num1][num2], end= ' ')
                            print()
                        print("--7")
                    elif trace4==special:
                        print("trace4")
                        for num1 in range(len(myarr)):
                            for num2 in range(len(myarr[num1])):
                                print(myarr[num1][num2], end= ' ')
                            print()
                        print("--7")
                    elif trace5==special:
                        print("trace5")
                        for num1 in range(len(myarr)):
                            for num2 in range(len(myarr[num1])):
                                print(myarr[num1][num2], end= ' ')
                            print()
                        print("--7")
                    elif trace6==special:
                        print("trace6")
                        for num1 in range(len(myarr)):
                            for num2 in range(len(myarr[num1])):
                                print(myarr[num1][num2], end= ' ')
                            print()
                        print("--7")
                    elif trace7==special:
                        print("trace7")
                        for num1 in range(len(myarr)):
                            for num2 in range(len(myarr[num1])):
                                print(myarr[num1][num2], end= ' ')
                            print()
                        print("--7")
                    elif trace8==special:
                        print("trace8")
                        for num1 in range(len(myarr)):
                            for num2 in range(len(myarr[num1])):
                                print(myarr[num1][num2], end= ' ')
                            print()
                        print("--7")
                    elif trace9==special:
                        print("trace9")
                        for num1 in range(len(myarr)):
                            for num2 in range(len(myarr[num1])):
                                print(myarr[num1][num2], end= ' ')
                            print()
                        print("--7")

def main(blist):
    tot = len(blist)
    for itrj in range(len(blist)):
        print("{} of {}".format(itrj, tot))
        pickedb = blist[itrj] # 1 picked
        alist = copy.deepcopy(blist)
        alist.remove(pickedb)
        for i in range(len(alist)-1,-1,-1):
            if alist[i][0]==pickedb[0]:
                alist.remove(alist[i])
        for i in range(len(alist)-1,-1,-1):
            if alist[i][1]==pickedb[1]:
                alist.remove(alist[i])
        for i in range(len(alist)-1,-1,-1):
            if alist[i][2]==pickedb[2]:
                alist.remove(alist[i])
        for i in range(len(alist)-1,-1,-1):
            if alist[i][3]==pickedb[3]:
                alist.remove(alist[i])
        for i in range(len(alist)-1,-1,-1):
            if alist[i][4]==pickedb[4]:
                alist.remove(alist[i])
        helper(alist)

                        
if __name__ == "__main__":
    ndim = 5
    blist = list(permutations(list(range(1,ndim+1)),ndim))
    main(blist)