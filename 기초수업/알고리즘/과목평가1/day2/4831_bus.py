K = 3
N = 10
M = 5
M_list = [1, 3, 5, 7, 9]

current = 0
count = 0

while count < M+1:
    print(count)
    if current + K >= N:
        break
    else:
        for j in range(current+K, current-1, -1):
            if j in M_list:
                current = j
                count += 1
                break

            else:
                count = 0
                break

