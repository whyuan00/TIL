
#
T = int(input())
for tc in range(1,T+1):
        a,b = list(input().split())

        # dic 는 {zrO: 중복 개수} 형태의 딕셔너리. key 가 0부터 9까지 오름차순 되어있음
        dic = {}
        default_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
        for idx, char in enumerate(default_list):
            dic[char] = idx

        # input 리스트의 요소와 dic key가 동일하면 value에 +1
        data = list(input().split())


        for i in data:
            if i in dic:
                dic[i] +=1

        print(f'#{tc}')
        for key, value in dic.items():
            if value != 0:
                print((key +' ') * dic[key], end =' ')
                print()






# print(dic)
# a_list = ["ZRO", "ONE", "TWO", "THR", "FOR"]
# for i in range(len(a_list)):
#     a_list[i] = dic[a_list[i]]
#
# print(a_list)
#
