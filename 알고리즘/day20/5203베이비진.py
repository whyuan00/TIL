

def triplet(lst):
    lst.sort()
    for i in lst:
        if lst.count(i) >= 3:
            return True
    return False

def runn(lst):
    for i in range(len(lst)):
        if lst[i] in lst and lst[i]+1 in lst and lst[i] +2 in lst:
            return True

    return False

T= int(input())
for tc in range(1,T+1):
    Nlst = list(map(int, input().split()))

    p1 = []
    p2 = []
    for i in range(len(Nlst)//2):
        p1.append(Nlst[i*2])
        p2.append(Nlst[i*2+1])

        if runn(p1) or triplet(p1):
            print(f'#{tc} 1')
            break

        elif runn(p2) or triplet(p2):
            print(f'#{tc} 2')
            break


    else:
        print(f'#{tc} 0')



