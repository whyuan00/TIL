'''
비트연산자
and : &
or : |

'''

print(6&5)

#bin, hex 는 각각 2진수/16진수 변환 내장함수
print(bin(10)) # 0b1010,
print(hex(10)) # 0xa

# int 함수로 문자열-> 숫자로 변환 가능
print(int('1011',2)) # 2진수 문자열을 10진수로 변환
print(int('b',16)) # 6진수 문자열을 10진수로 변환


print(0b11011110 & 0b11011) # and
print(0x4A3|25) # or 1911


# ^ 'xor' 연산자: 같으면 0 다르면 1
# XOR 두번하면 원래수 돌아옴 -> 암호화에 사용 가능
#  암호화 함수 en, 디코딩 함수 de
'''
def en (N):
    return (N ^ 1004)

def de(N):
    return (N ^ 1004)
'''
key = 1004
def encode_decode(N):
    return N ^ key

# print(encode_decode(N))

'''
<< 비트열 왼쪽 이동
>> 비트열 오른쪽 이동 

ex. i<<N : N만큼 왼쪽으로 밀고 빈공간 0으로 채움
'''
print(bin(0b100<<2))
print(bin(0b100>>2))

# << 이용해서 반복문 가지고 출력

for i in range(5):
    print(bin(0b1<<i), 0b1<<i)
    # int('str',2) 문자열일때 만 진수 필요, 아니면 그냥 int

t = 1
for i in range(5):
    print(bin(t), t)
    t= t<<1

# 1<<n 은 2의 n제곱값

(i & (1<<N)) # i의 N번 비트가 1인지 확인
'''
0보다 큰수로 & 연산자를 했을때 값이 양수면 n번 비트는 1 (True)
0보다 큰수로 & 연산자를 했을때 값이 0이면 n번 비트는 0 (False)

p = 100
for i in range(5):
    print( p &(1<< i), i)
'''


# 음수
'''
음수표현법:
음수는 2의 보수로 관리 

MSB는 음수 양수 구분 비트 -> 2진수의 가장 앞자리 
1이면 음수 0이면 양수 

'''
# 5를 바꾸는 방법: 1. 5를 이진수로
# 2. 2의 보수는 msb 1로바꾸기
# 3. msb 빼고 나머지 1 or 0 을 모두 뒤집은다음에 +1
# ex. 0000 0101 -> 1000 0101 -> 1111 1010 -> + 1 = 1111 1011

# 초기화 하면 똑같이 하나?

'''
Not 연산자: 모든비트 반전 
'''
print(~4) # -5
bin(4) # 0b100 -> 양수니까 0100
# not 연산자: 1011 : msb는 =1 음수, 나머지 bit는 011
#나머지에 bit에 2의 보수취하면 1100+1 = 1101= 5


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())# N은 M이진수 표현의 마지막 N bit

    for i in range(N):
        if M & (1<<i):
            pass
        else:
            print(f'#{tc} OFF')
            break
    else:
        print(f'#{tc} ON') # for 문이 정상적으로 돌아가면 else 로 옴

# 선생님 풀이
def Test():
    tar = M
    for i in range(N):
        if tar & 0x1 ==0:  # 10진수 1 표시 위해 0x1
            return False
        tar = tar>>1  # tar뒷자리 하나씩 없애기
    return True

