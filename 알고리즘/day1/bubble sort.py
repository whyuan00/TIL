


def bubble_sort(a,arr):
    for i in range(a-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort(8,[1,4,1,6,9,3,0,7]))