def selection_sort(arr):
    """Sorts a list in ascending order using Selection Sort. O(n^2)."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11, 90, 5]
    print("Original:", sample)
    print("Sorted:  ", selection_sort(sample))
