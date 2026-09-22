def upperBound(arr, target):
    low = 0
    high = len(arr) - 1
    result = len(arr)
    while left <= right:
        mid = low + (hight - low) // 2
        # we compare with the lower bound and see if its equal then there is a posible soultion on the right
        if arr[mid] > target:
            result = mid
            high = mid - 1
        else: 
            low = mid + 1


        return result