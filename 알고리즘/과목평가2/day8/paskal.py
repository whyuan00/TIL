

N = int(input())
arr = []
for i in range(1,N+1):
    arr.append([ 0 for _ in range(i) ])

print(arr)

#재귀함수

def paskal(N,arr):
    for i in range(N):
        for j in range(N):
            if N == 1:
                arr[0][0] = 1
                return arr
            else:
                if j== 0 or j== N-1 :
                    arr[i][j] ==1

                else:
                    for i in range(N):
                        for j in range(N):
                            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


    return arr

#
#
#     else:
#         1 + paskal(N-1) + 1

print(paskal(N,arr))