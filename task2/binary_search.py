def binary_search(array, target):
    left = 0
    right = len(array) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return iterations, array[mid]

    # If the target is not found, return the upper bound
    upper_bound = array[left] if left < len(array) else None
    return (iterations, upper_bound)


