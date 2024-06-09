T= int(input())
for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))

    left = -1
    right = N
    left_sum = 0
    right_sum = 0

    while left < right:
        if left_sum < right_sum:
            left += 1
            if left < right:
                left_sum += a[left]
            else:
                left -= 1
                break

        else:
            right -= 1
            if left < right:
                right_sum += a[right]
            else:
                right += 1
                break

    result = abs(left_sum-right_sum)

    print(f'#{tc} {left+1} {result}')