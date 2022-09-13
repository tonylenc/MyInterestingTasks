def binary_search(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1
