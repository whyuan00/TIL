'''
선형큐 문제점:
삽입삭제 계속할때
front 의 앞부분이 비어있어도 front= N-1 즉 포화로 인식하고 삽입안함
'''


'''
원형큐:
1차원배열의 처음과 끝이 연결되어 원형 이룬다고 가정 

초기 공백 front = rear = 0


-> front와  rear 가 n-1 이휴에 다시 0으로 이동 
front 자리는 빈자리로 둠

원형 큐 삽입위치는 rear = (rear+1)mod n        #선형은 rear+1
원형 큐 삭제위치는 front = (front+1)mod n       #선형은 front +1 
'''
# 공백은 여전히 front == rear
# 꽉차있는 상태는 front == (rear+1) % N 으로 판단
# 포화는 rear 다음이 현재 front (front는 비워둬야하기 때문)


'''
포화나 공백상태가 아닐때: rear 와 front 값 조정해서 새로운 원소 삽입자리 마련 
삽입시 rear = (rear+1) % n
삭제시 front = (front+1) % n


'''
#삭제
def 삭제():
    global front
    if isEmpty(): # def isEmpty(): return front = rear / isFull(): return (rear+1) % N  == front
        print()
    else:
        front = (front +1) % N
        return arr[front] # 새로운 front 값을 return 해서 삭제와 동일 기능 cf. pop()