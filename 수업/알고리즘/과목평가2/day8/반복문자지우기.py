
# 인덱스 다음으로 이동, 해당 인덱스에 item 넣기
def push(item, stack,size):
    global top
    top +=1
    if top == size:
        return 'overflow'
    else:
        stack[top] = item

# 최근 데이터 출력하고 인덱스 이전으로 이동
def pop():
    global top
    if top == -1:
        return 'underflow'
    else:
        top -= 1
        return stack[top+1]

T = int(input())
for tc in range(1,T+1):
    a = input()
    size = len(a)
    stack = [0] * (size+1)
    top = 0
    for char in a:
        if top == -1:  # 왜 stack[top] ==0 으로 하면 안되는지??
            push(char,stack,size)

        if stack[top] != char:
            push(char,stack,size)

        elif stack[top] == char:
            pop()
    print(f'#{tc} {top}')

# a = 'UKJWHGGHNFTCRRCTWLALX' # 5
# N = len(a)
# b = []
#
# for i in a:
#     if b: # b가 비어있는지 아닌지
#         if b[-1] != i:
#             b.append(i)
#         else:
#             b.pop()
#     else:
#         b.append(i)
#
# print(b)
