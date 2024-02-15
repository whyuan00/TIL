
N = 10
q = [0] * N
front = rear = -1

rear +=1
q[rear] = 10 # a.append(10)

rear +=1
q[rear] = 20

rear +=1
q[rear] = 30

while front != rear: #큐 비어있지 않으면
    front +=1
    print(q[front]) # q.pop(0)
