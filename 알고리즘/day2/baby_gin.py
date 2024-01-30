# 완전검색

num = 456789
c = [0] * 12

# 넘의 1의자리 인덱스에 +1
# 넘은 10으로 나눠서 재할당

while num > 0:
    for i in range(6):
        c[num % 10] += 1
        num //= 10
print(c)

i = 0
tri = run = 0
while i<10:
    if c[i] >=3:
        c[i] -=3
        tri +=1
        continue

    if c[i]> 1 and c[i+1]>=1 and c[i+2]>=1: # 여기 range 때문에 c를 12칸 만듦. 만든후 데이터 삭제해줌
        c[i] -=1
        c[i+1] -=1
        c[i+2] -=1
        run +=1
        continue
    i+=1

if run + tri ==2: print("Baby Gin")
else:
    print("lose")





#
# def baby_gin(arr):
#
#     N = len(arr)
#     K = max(arr) +1
#     count = [0] * (K+1)
#
#     result = []
#
#     for i in arr:
#         count[i] += 1
#
#     for i in count:
#         if i == 3:
#             result.append('triplet')
#             count[i] -= 3
#             break
#
#     for i in range(1,K):
#         if count[i-1] and count[i] and count[i+1] == 1:
#             result.append('run')
#             break
#
#     if 'triplet' in result:
#         if 'run' in result:
#             return True
#     else:
#         return False
#
# arr = [7,2,3,4,7,7]
# print(baby_gin(arr))
