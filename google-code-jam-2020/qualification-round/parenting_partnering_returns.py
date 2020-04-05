# import gc

def main():
    listofsets = []
    j = set()
    c = set()
    n = int(input())
    res = ''
    for _ in range(n):
        inarr = input().split(' ')
        listofsets.append(set(range(int(inarr[0]), int(inarr[1]))))
    for s in listofsets:
        if s & j & c != set():
            print("Case #{}: {}".format(casenum, "IMPOSSIBLE"))
            return
        elif s & j == set():
            j |= s
            res += 'J'
        elif s & c == set():
            c |= s
            res += 'C'
        else:
            raise ValueError('UNEXPECTED ELSE')
    print("Case #{}: {}".format(casenum, res))


t = int(input())
casenum = 1

while casenum<=t:
    main()
    casenum += 1
    # gc.collect()

#test
'''

'''