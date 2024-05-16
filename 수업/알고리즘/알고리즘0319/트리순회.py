'''
트리는 싸이클 없는 무방향 연결 그래프 & 1:n으로 연결된 비선형&계층형 구조

1. 노드 사이에는 유일한 경로만 존재
2. 각 노드는 최대 하나의 부모노드 존재
3. 각 노드는 자식노드 없거나 여러개
'''

'''
전,중,후 순회 
'''
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,child):
        if not self.left:
            self.left = child
            return
        if not self.right:
            self.right = child
            return
        # 삽입 살패
        return

    def inorder(self):
        if self != None:
            if self.left:
                self.left.inorder()

            print(self.value, end=' ') # 전위순회

            if self.right:
                self.right.inorder()


# 이진트리 만들기
#1.노드생성
nodes = [TreeNode(i) for i in range(0,14)]
#2. 간선연결
for i in range(0,len(arr),2):
    p = arr[i]
    c = arr[i+1]
    nodes[p].insert(nodes[c])

nodes[1].inorder()



#코테용
def inorder(n):
    if  not n:
        return
    inorder(nodes[n][0])
    print(n, end=' ')
    inorder(nodes[n][1])

nodes = [[] for _ in range(14)]
for i in range(0,len(arr),2):
    p = arr[i]
    c = arr[i+1]
    nodes[p].append(c)

# 자식이 없으면 None
for li in nodes:
    for _ in range(len(li),2): # li가 0이면 2개, 1이면 1개, 2면 0개 넣음
        li.append(None)
print()
inorder(1)



