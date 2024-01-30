K = 3
N = 10
M = 5
M_list = [1, 3, 5, 7, 9]

현재 = 0
count = 0

while count <M:
    if 현재 + K >= N:
        print(현재)
        break

    else:
        if 현재 + K > M_list[count]:
            현재 = M_list[count]
            count += 1
            print(현재)
        else:
            count = 0
            break

print(count)

