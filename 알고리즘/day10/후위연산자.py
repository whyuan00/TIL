
fx = '(6+5*(2-8)/2)'
postfx = ''

top = -1
st = [0] * 100

icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 기본 연산자 순서
isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택안의 연산자 순서는 괄호 순서 바뀜

for tk in fx:

    #토큰이 여는 괄호면 push 아니면 연산자고 현재 st의 top 원소보다 우선순위 높으면 push
    if tk == '(' or (tk in '+-*/' and isp[st[top]] < icp[tk]):
        top +=1
        st[top] = tk #push

    # 연산자이고 top보다 우선순위 높지 않으면
    elif tk in '+-*/' and isp[st[top]] >= icp[tk]:

        # top보다 우선순위가 낮을때까지 pop해서 postfx 에 붙여줌
        while  isp[st[top]] >= icp[tk]:
            top -=1
            postfx += st[top+1]

        #pop 한다음에  push
        top +=1
        st[top] = tk
    elif tk == ')': #닫는 괄호면 여는괄호 만날때까지 pop
        while st[top] != '(':
            top -=1
            postfx += st[top+1]
        top -=1  # 여는괄호는 버림

    else: #피연산자인경우 출력
        postfx += tk

print(postfx)


        