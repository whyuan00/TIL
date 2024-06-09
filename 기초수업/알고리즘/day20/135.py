def triplet(lst):
    lst.sort()
    for i in lst:
        if lst.count(i) >= 3:
            return True
    return False

def run(lst):
    for i in range(len(lst)):
        if lst[i] and lst[i]+1 and lst[i] +2 in lst:
            return True

    return False

lst = [1,4,5,5,9,2]

print(run(lst))