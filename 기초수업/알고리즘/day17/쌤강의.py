'''
>>> print(f'{149:08b}')
10010101
>>> print(f'{75:08b}')
01001011
>>> print(f'{149:04x}')
0095
>>> print(f'{15:04X}')
000F
>>> print(f'{15:04x}')
000f
>>> print(hex(15))
0xf
>>> print(int('15', 16))
21
>>> print(f'{75:#04x}')
0x4b
'''



# bit(N-1) 자리수 부터 0까지 모두 1인숫자
'''
N, M = map(int,input().split())

#현재 b는 N-1 자리수까지 모두 1인 이진수
b = (1<<N) -1  # N=4 일때 10000 -1 = 0000 1111

#b 확인 원할경우 이진수로 뱉으라고 하기
#print(f'{b:04b}') #자리수 표시 / b = 2진법으로 뱉기

 # and 연산자: 공통값 구한 결과가 b 이면 ON
if M &b == b:
    print(f"#{tc} ON")
else:
    print(f"#{tc} OFF")

'''

# 음수표현

