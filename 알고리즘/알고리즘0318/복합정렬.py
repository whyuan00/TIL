



import sys
sys.stdin = open('input (3).txt','r')


def merge(left,right):
    res = [0]* (len(left) + len(right))
    i = j = 0
    while i< len(left) and j< len(right):
        if left[i] < right[j]:
            res[i+j] = left[i]
            i+=1
        else:
            res[i+j] = right[j]
            j+=1

    # i,j 집어넣고 나오기: i,j 인덱스 이동상황
    while i< len(left):
        res[i+j] = left[i]
        i += 1
    while j < len(right):
        res[i+j] = right[j]
        j+=1
    return res


def ms(m):
    if len(m) == 1:
        return m
    # else:
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]
    left = ms(left)
    right = ms(right)

    return merge(left, right)



A = list(map(int,input().split()))
A = ms(A)
print(A[500000])






