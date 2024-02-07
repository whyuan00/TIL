

##### 딕셔너리로 푸는 방법 



def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    if top == -1:   # -1인 상태가 underflow
        return 0
    else:
        top -= 1
        return stack[top+1]

T = int(input())
for tc in range(1,T+1):
    top = -1   # top 을 계속 초기화 해줘야함
    a = input()
    N = len(a)
    stack = [0] * (N+1)

    def f(a):
        for char in a:
            # print(stack)
            # print(top)
            if char == '(' or char =='{':
                push(char)



            elif char == ')':
                if top != -1 and stack[top] == '(':  # pop 할때 다른 것도 사라질 수 있음
                    pop()
                else:
                    return 0

            elif char == '}':
                if top != -1 and stack[top] == '{':
                    pop()
                else:
                    return 0
            else:
                pass



        if top != -1:  #스택안에 데이터가 남아있을 경우
            return 0
        else:
            return 1

    print(f'#{tc} {f(a)}')


