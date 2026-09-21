def binarySearch(arr, targetValue):
    left = 0
    right = len(arr) - 1

    while left <= right: 
        mid = (left + right)//2;

        if(arr[mid] == targetValue):
            return mid
        
        if arr[mid] < targetValue:
            left = mid + 1

        else: 
            right = mid - 1

    return -1

myList = [1,3,5,6,9,11,13,15,17,19]
x = 11

result = binarySearch(myList, x)

if result != -1:
    print("Found at index", result)
else:
    print("nothing found")