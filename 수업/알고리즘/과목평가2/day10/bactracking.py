'''

백트래킹은 해찾다 막히면 되돌아가서 찾기.
최적화
결정 ex. 조건 만족해가 존재하는지 yes or no
문제 해결에 이용
'''

def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end = ' ')
        print()
    else:
        #make candidate 말고 직접 구현 가능
        # for j in range(2): #두개밖에 없으니까 2? 후보군 두개 골라서 차례대로 넣어주기
        #     bit[i] = j
        #     f(i+1, k)

        bit[i] = 1  #후보 0또는 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)

N = 4
arr = [1,2,3,4]
bit = [0] * N #bit[i] : arr[i]가 부분집합에 포함되었는지 체크하는 배열

f(0,N) # bit[i] 에 1또는 0 채우고 N개 원소가 결정되면 부분집합 출력
