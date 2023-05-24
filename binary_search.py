def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target element not found

# Example usage:
array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 38

index = binary_search(array, target)

if index != -1:
    print("Target element ",target ,"found at index", index,"\n")
else:
    print("Target element not found in the array.")
