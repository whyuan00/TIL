'''
수영장 dp로 풀수있음
1. 작은 문제로 분할
2. 정수로 쪼개기
3. 뒤의 결과 구할때 앞에서 구했던 결과 바뀌면 안됨
'''

T = int(input())

for tc in range(1,T+1):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int,input().split()))

    # dp배열
    plans = [0]* 13
    # 12월 반복
    for i in range(1,13):
        # 이전달 + 1일권, 이전달+1달권 , 3달전 +3달권 나눠서 생각