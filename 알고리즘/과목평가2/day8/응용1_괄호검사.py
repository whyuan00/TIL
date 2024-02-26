#대괄호 [] 중괄호{} 소괄호 ()
# 개수 같아야함, 왼쪽이 먼저 나와야함, 괄호사이에는 포함만 존재
# 스택이용해서 검사 가능

#여는 괄호 보면 스택에 넣기, 닫는 괄호 만나면 pop 해서 동일한지 비교
#top 포인터 이동해가면서 표시함, 지나친 자리에 파일 들어오면 덮어씌워지니까 지울필요 x


def push(item, stack, size):
    global top
    top +=1
    if top == size:
        return False
    else:
        stack[top+1] = item

def pop():
    global top
    top -= 1
    if top == -1:
        return False
    else:
        return stack[top+1]


def f(a):
    for i in a:
        if i == '(':
            push(i,stack,size)
        else:
            if pop() != i:
                return False

    return True

top = -1
a = '(()))'
size = len(a)
stack = [0] * (size+1)
print(f(a))