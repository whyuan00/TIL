
def push(x):
    global top
    top += 1
    st[top] = x

def pop():
    global top
    if top == -1:
        return 'error'
    else:
        top -=1
        return st[top+1]

T = int(input())
for tc in range(1, T+1):
    a = list(input().split())
    top = -1
    st = [0]* len(a)

    def f():
        global a
        global top
        global st

        for char in a :
            if char.isdigit():
                char = int(char)
                push(char)

            elif char == '.':
                if top == 0:
                    return st[top]
                else:
                    return 'error'

            else:
                if top <1:
                    return 'error'
                else:
                    if char == '+':
                        x = pop()
                        y = pop()
                        push(x+y)

                    if char == '-':
                        x = pop()
                        y = pop()
                        push(y - x)

                    if char == '*':
                        x = pop()
                        y = pop()
                        push(x * y)

                    if char == '/':
                        x = pop()
                        y = pop()
                        push(y // x)

    print(f"#{tc} {f()}")