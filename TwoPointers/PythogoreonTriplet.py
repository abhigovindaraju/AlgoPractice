def findPyTriplet(arr):
    triplet = []
    current_sum = 0
    arr.sort()
    arr = arr[::-1]
    print(arr)
    for i in range(0, len(arr) - 1):
        left = i + 1
        right = len(arr) - 1
        while (left < right):
            current_sum = arr[left] ** 2 + arr[right] ** 2
            print (current_sum, arr[i]**2)
            if(current_sum == arr[i] ** 2):
                triplet.append([arr[i], arr[left], arr[right]])
                return triplet
            elif (current_sum > arr[i]):
                right -= 1
            else:
                left = left + 1
    
    return -1
    

arr = [3, 1, 4, 6, 5]
print(findPyTriplet(arr))
