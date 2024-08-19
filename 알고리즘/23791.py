# h행 w열에 m,n 차이나게 넣기
H,W,N,M = map(int, input().split())

if H//(N+1) == H/(N+1):
    row = H//(N+1)
else:
    row = H//(N+1)+1

if W // (M + 1) == W/ (M + 1):
    col = W // (M + 1)
else:
    col = W // (M + 1) + 1

print(row*col)