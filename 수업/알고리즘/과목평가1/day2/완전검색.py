# {1,2,3}포함하는 모든 순열 생성함수

for x in range(1,4):
    for y in range(1,4):
        if y != x:
            for z in range(1,4):
                if z != x and z != y:
                    print(x, y, z)