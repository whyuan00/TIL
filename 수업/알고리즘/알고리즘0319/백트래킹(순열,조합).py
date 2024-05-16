# 백트래킹

'''
def dfs(lv):
    if lv == 3:
        print(''.join(map(str,path)))
        return

    #branch 도 3
    else:
        for j in arr:
            path.append(j)
            dfs(lv+1)
            path.pop()

arr= [i for i in range(1,4)]
path = []
dfs(0)

'''
# 중복없는 순열
'''
def dfs(lv):
    if lv == 3 and len(path)==3:
        res.append((''.join(map(str,path))))
        return

    #branch 도 3
    else:
        for j in arr:
            if j not in path:
                path.append(j)
                dfs(lv+1)
                path.pop()

arr= [i for i in range(1,4)]
path = []
res = []
dfs(0)
print(res)
'''


def dfs(level):
    if level ==3:
        print(path)
        return

    for i in range(len(arr)):
        if arr[i] in path:
            continue
        # append 말고 인덱싱이 더 빠름 
        path[level] = arr[i]
        dfs(level+1)
        path[level] = 0

arr= [i for i in range(1,4)]
path = [0]*3
dfs(0)