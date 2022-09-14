def binary_search(seq, x):
    left = 0
    right = len(seq) - 1

    while left <= right:
        mid = (left + right) // 2

        if seq[mid] == x:
            return mid

        elif seq[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def left_binary_search(seq, x):  # (left, right]
    left = -1
    right = len(seq) - 1

    while right - left > 1:
        mid = (left + right) // 2

        if seq[mid] >= x:
            right = mid
        else:
            left = mid

    return right


def right_binary_search(seq, x):  # [right, left)
    left = 0
    right = len(seq)

    while right - left > 1:
        mid = (left + right) // 2

        if seq[mid] > x:
            right = mid
        else:
            left = mid

    return left
