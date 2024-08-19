dp = [1] * 10001

# 중복을 허용하지 않는 dp
for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])
'''

T = int(input())
for tc in range(1,T+1):

    n = int(input())
    res= [0,0,0]
    res_list = []
    def dfs(n,res):
        if n<=0:
            if res not in res_list:
                res_list.append(res[:])
            return
        # -1
        if n-1>=0:
            n-=1
            res[0]+=1
            dfs(n,res)
            n+=1
            res[0]-=1
        # -2
        if n-2>=0:
            n-=2
            res[1]+=1
            dfs(n,res)
            n+=2
            res[1]-=1
        # -3
        if n-3>=0:
            n-=3
            res[2]+=1
            dfs(n,res)
            n+=3
            res[2]-=1
        else:
            return
    dfs(n,res)
    print(len(res_list))

'''
