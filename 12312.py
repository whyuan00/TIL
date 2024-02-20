
row, col = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
print(arr)

test = []
test.extend(arr)

for j in range(row):
    arr[j] = [0]* col
    print(arr)

    arr = test
    arr[j] = [1]* col
    print(arr)

    arr = test

