def lowerBound(arr, targetValue):
    left = 0
    right = len(arr) - 1
    result = len(arr)
    while left <= right:
        mid = (left + right) // 2
        # [2, 3, 7, 10, 11,11 25] target = 9
        # 7 is the length low is 0 and right is 6 therefore mid = 3
        # if the mid of the array is greater than or equal ot the upper bound
        # mid can be the result but right is set mid - 1 to check teh lower bound
        if arr[mid] >= target:
            result = mid
            right = mid - 1
        else: 
            left = mid + 1

        return result
