import sys
input = sys.stdin.readline
s = input().strip()
t = input().strip()

def dfs(s,t):
    if t==s:
        print(1)
        exit()
    # A 빼기
    if t[-1] == 'A' and len(t)-1>0:
        dfs(s,t[:-1])
    if t[0] =='B'and len(t)-1>0:
        dfs(s,t[::-1][:-1])

dfs(s,t)
print(0)

# reverse 는 list 뒤집음
'''
def dfs(s,t):
    global res
    if len(s)>len_t:
        return
    if s==t:
        res = True
        return

    if len(s+'A')<=50:
        dfs(s+'A',t)
    new = s+'B'
    if len(new)<=50:
        dfs(new[::-1],t)

dfs(s,t)
if res:
    print(1)
else:
    print(0)
'''
