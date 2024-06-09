
#



di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 3
arr = [[1,2,3],[4,5,6],[7,8,9]]
newarr = [[0]* (N) for _ in range(N)]


for i in range(N):
    for j in range(N): # i = 0
        while True:

            ni = i + di[0]
            nj = j + dj[0]
            print(ni, nj)




print(newarr)