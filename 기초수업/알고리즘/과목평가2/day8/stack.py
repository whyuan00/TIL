#stack
# push 와 pop -> 후입선출
# isEmpty: 스택이 공백인지 확인
# peek: 스택의 top 원소 반환

def push(item,size):
    global top
    top +=1
    if top == size:
        print('overflow!') # stack 에 저장공간 없으면 오버플로우
    else:
        stack[top] = item # 공간 있으면 top 공간에 item 넣기

size = 10
stack = [0]*size
top = -1

push(10,size)
top+=1
stack[top] = 20



def pop():
    global top
    if top ==-1:
        print('underflow')
        return 0
    else:
        top -=1
        return stack[top+1]
print(pop())

# 직접 구현시
if top >-1:
    top -=1
    print(stack[top+1])