

# dict = {B: 11, CDEF...XYZ}

# for i in len(new_list):
#     sum = 0
#     if n[i] <=10:
#         sum += b**i * N[i]


# print(sum)


N = input()
b = int(input())

new_list = (N)[::-1]  # 한 글자씩 거꾸로 list

dict_alpha = {}
for i in range(26):
    key = chr(ord('A') + i)     # 알파벳 A부터 Z까지 순서대로 키 생성
    value = 10 + i              # 10부터 35까지의 값을 값으로 사용
    dict_alpha[key] = value


sum = 0

for idx, char in enumerate(new_list):
    if char.isalpha() == True:
        numb = (b ** idx) * dict_alpha[char]   # new_list 가 알파벳이면 키 값 불러와서 계산 
        sum += numb 
    
    else:
        numb = (b ** idx) * char   # new_list 가 숫자면 바로 계산 
        sum += numb

print(sum)