def binary_search(arr, target):
    """Returns the index of target in a SORTED list, or -1 if not found. O(log n)."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    sorted_arr = [5, 11, 12, 22, 25, 64, 90]
    target = 22
    index = binary_search(sorted_arr, target)
    print(f"Searching for {target} in {sorted_arr}")
    print(f"Found at index {index}" if index != -1 else "Not found")
