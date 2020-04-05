import math
def main(arg0, arg1):
    # t = sys.argv[0]
    # n = sys.argv[1]
    t = int(input())
    n = int(input())
    i=1
    c1 = math.floor(n/2)
    c2 = math.ceil(n/2)
    while has4(c1) or has4(c1):
        c1-=1
        c2+=1
    print("Case #{}: {} {}".format(i,c1,c2))
    return None

def has4(num):
    while num > 0:
        if num % 10 == 4:
            return True
        num//=10
    return False


if __name__ == "__main__":
    main()


