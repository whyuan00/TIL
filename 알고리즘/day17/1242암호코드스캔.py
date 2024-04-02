import copy

def find(arr): #  arr 문자열에서 암호 뽑는 함수
    key = ''
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '0':
                n1 = j
                i_lst.append(i)
                for k in range(M-1,-1,-1):
                    if arr[i][k] != '0':
                        n2 = k
                        key += arr[i][n1:n2+1]
                        key_lst.append(arr[i][n1:n2+1])
                        return key

def change_find(arr):
    key = find(arr) # 6EED19376EC58D
    for i in range(N):
        arr[i] = arr[i].replace(key, '0' *len(key)) # 해당 열 전부 0으로 바꾸기

    return arr # 하나의 key 빼고 다시  뱉기

# T = int(input())
# for tc in range(1,T+1):
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
arrnew = copy.deepcopy(arr)
key_lst = []
i_lst = [] # 행 번호 저장

# 반복으로 key_lst 뽑기
while True:
    try :
        change_find(arrnew)
    except:
        break
# print(key_lst): ['6EED19376EC58D', '1E06079861E79F99FE079861E79F8']

# for i in key_lst:
#     key_lst[key_lst.index(i)] = (bin(int(i,16))[2:])
# # print(key_lst) : ['110111011101101000110010011 ...
# # print(i_lst) : [17, 173]


bin_key_lst = []
num_key = len(key_lst) # = len(i_lst)
for i in range(num_key): #암호 개수만큼 반복
    arr[i_lst[i]] = arr[i_lst[i]].replace(key_lst[i], bin(int(key_lst[i],16))[2:])
    bin_key_lst. append(arr[i_lst[i]])

# print(bin_key_lst): ['이진법행', ...]

k = 1
dic = {'0'*3*k+'1'*2*k+'0'*1*k+'1'*1*k: '0',
       '0'*2*k+'1'*2*k+'0'*2*k+'1'*1*k: '1',
       '0'*2*k+'1'*1*k+'0'*2*k+'1'*2*k: '2',
       '0'*1*k+'1'*4*k+'0'*1*k+'1'*1*k: '3',
       '0'*1*k+'1'*1*k+'0'*3*k+'1'*2*k: '4',
       '0'*1*k+'1'*2*k+'0'*3*k+'1'*1*k: '5',
       '0'*1*k+'1'*1*k+'0'*1*k+'1'*4*k: '6',
       '0'*1*k+'1'*3*k+'0'*1*k+'1'*2*k: '7',
       '0'*1*k+'1'*2*k+'0'*1*k+'1'*3*k: '8',
       '0'*3*k+'1'*1*k+'0'*1*k+'1'*2*k: '9',
}

ans_lst = []
for i in bin_key_lst:
    for n in range(len(i)-7):
        ans = ''
        if i[n:n+7*k] in dic:
            for _ in range(8):


#         else:
#             k+=1
# print(ans_lst)


