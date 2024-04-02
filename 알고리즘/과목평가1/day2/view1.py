import sys

# 컴퓨터 입력 연결 통로. 원래 콘솔이랑 연결되어 있지만 입력을 파일로 바꾸는 거
sys.stdin = open('input.txt', 'r')


TC = 1
for tc in range(1,TC+1):
    N = int(input()) # 건물개수
    N_list = list(map(int,input().split())) # 건물 높이 리스트

    total = 0
    for i in range(2, N-2):

        for j in [i-2, i-2, i+1, i+2]:
            max_height = 0

            if N_list[i] > N_list[j]:
                height = N_list[i] - N_list[j]

                if height > max_height:
                    max_height = height

