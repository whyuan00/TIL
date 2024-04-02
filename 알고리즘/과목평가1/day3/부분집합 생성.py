
arr = [1,2,3,4]
bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l

                for p in range(4):
                    if bit[p] == 1: # bit의 0~3 인덱스에 대해 할당된 값이 1일때 arr에서 동일 인덱스 가져옴
                        print(arr[p])
                print()
