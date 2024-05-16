# 16진수 dic
dic16 = {}
for i in range(65,72):
    dic16[chr(i)] = i - 55


# 10진수를 2진수 만드는 재귀
def make(a): # 47이런거일때
    last = str(a%2)
    a = a//2
    if a ==0:
        a = str(a)
        return a + last
    else:
        return  make(a) + last


def change(x):
    ans = ''
    for i in x: #x = '47FE'
        if i.isdigit():
            i = int(i)
            res = make(i)
            if len(res) < 4:
                res = '0'*(4-len(res)) + res
            if len(res) > 4:
                res = res.replace('0','',1)
            ans += res

        else:
            i = int(dic16[i])
            res = make(i)
            if len(res) < 4:
                res = '0'*(4-len(res)) + res
            if len(res) > 4:
                res = res.replace('0','',1)
            ans += res
    return ans



T = int(input())
for tc in range(1,T+1):
    n, x = input().split()
    print(f'#{tc} {change(x)}')


