#check latin squares 5
#input
#2
#1 2 2 1
n = 5

from itertools import permutations


biglist = list(permutations(list(permutations([1,2,3,4,5])), 5))

for idx in range(len(biglist)):
    nums = []
    arr = biglist[idx]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            nums.append(arr[i][j])
    if all([(len(set([nums[i*n+x]for x in range(n)])) == n)*(len(set([nums[i+n*x]for x in range(n)])) == n)for i in range(n)]):
        #is latin square
        trace0 = biglist[idx][0][0] + biglist[idx][1][1] + biglist[idx][2][2] + biglist[idx][3][3] + biglist[idx][4][4]
        # trace1 = biglist[idx][0][1] + biglist[idx][1][2] + biglist[idx][2][3] + biglist[idx][3][0]
        # trace2 = biglist[idx][0][2] + biglist[idx][1][3] + biglist[idx][2][0] + biglist[idx][3][1]
        # trace3 = biglist[idx][0][3] + biglist[idx][1][0] + biglist[idx][2][1] + biglist[idx][3][2]

        # trace4 = biglist[idx][3][0] + biglist[idx][2][1] + biglist[idx][1][2] + biglist[idx][0][3]
        # trace5 = biglist[idx][3][1] + biglist[idx][2][2] + biglist[idx][1][3] + biglist[idx][0][0]
        # trace6 = biglist[idx][3][2] + biglist[idx][2][3] + biglist[idx][1][0] + biglist[idx][0][1]
        # trace7 = biglist[idx][3][3] + biglist[idx][2][0] + biglist[idx][1][1] + biglist[idx][0][2]
        # if trace0 == 5 or trace0 == 6 or trace0 == 7 or trace0 == 9 or trace0 == 10 or trace0 == 11 or trace0 == 13 or trace0 == 14 or trace0 == 15 or trace1 == 5 or trace1 == 6 or trace1 == 7 or trace1 == 9 or trace1 == 10 or trace1 == 11 or trace1 == 13 or trace1 == 14 or trace1 == 15 or trace2 == 5 or trace2 == 6 or trace2 == 7 or trace2 == 9 or trace2 == 10 or trace2 == 11 or trace2 == 13 or trace2 == 14 or trace2 == 15 or trace3 == 5 or trace3 == 6 or trace3 == 7 or trace3 == 9 or trace3 == 10 or trace3 == 11 or trace3 == 13 or trace3 == 14 or trace3 == 15 or trace4 == 5 or trace4 == 6 or trace4 == 7 or trace4 == 9 or trace4 == 10 or trace4 == 11 or trace4 == 13 or trace4 == 14 or trace4 == 15 or trace5 == 5 or trace5 == 6 or trace5 == 7 or trace5 == 9 or trace5 == 10 or trace5 == 11 or trace5 == 13 or trace5 == 14 or trace5 == 15 or trace6 == 5 or trace6 == 6 or trace6 == 7 or trace6 == 9 or trace6 == 10 or trace6 == 11 or trace6 == 13 or trace6 == 14 or trace6 == 15 or trace7 == 5 or trace7 == 6 or trace7 == 7 or trace7 == 9 or trace7 == 10 or trace7 == 11 or trace7 == 13 or trace7 == 14 or trace7 == 15:
        #     print("FOUND")
        #     print(biglist[idx])
        if trace0==6:
            for num1 in range(len(biglist[idx])):
                for num2 in range(len(biglist[idx][num1])):
                    print(biglist[idx][num1][num2], end= ' ')
                print()
            print("--6")
        if trace0==7:
            for num1 in range(len(biglist[idx])):
                for num2 in range(len(biglist[idx][num1])):
                    print(biglist[idx][num1][num2], end= ' ')
                print()
            print("--7")
        if trace0==23:
            for num1 in range(len(biglist[idx])):
                for num2 in range(len(biglist[idx][num1])):
                    print(biglist[idx][num1][num2], end= ' ')
                print()
            print("--23")
        if trace0==24:
            for num1 in range(len(biglist[idx])):
                for num2 in range(len(biglist[idx][num1])):
                    print(biglist[idx][num1][num2], end= ' ')
                print()
            print("--24")
        

# nums = [int(x) for x in input().split()]
# for

# 1, 2, 3, 4
# 1, 2, 4, 3
# 1, 3, 2, 4
# 1, 3, 4, 2
# 1, 4, 2, 3
# 1, 4, 3, 2
# 2, 1, 3, 4
# 2, 1, 4, 3
# 2, 3, 1, 4
# 2, 3, 4, 1
# 2, 4, 1, 3
# 2, 4, 3, 1
# 3, 1, 2, 4
# 3, 1, 4, 2
# 3, 2, 1, 4
# 3, 2, 4, 1
# 3, 4, 1, 2
# 3, 4, 2, 1
# 4, 1, 2, 3
# 4, 1, 3, 2
# 4, 2, 1, 3
# 4, 2, 3, 1
# 4, 3, 1, 2
# 4, 3, 2, 1



# if all([(len(set([nums[i*n+x]for x in range(n)])) == n)*(len(set([nums[i+n*x]for x in range(n)])) == n)for i in range(n)]):
#     pass #is latin square
