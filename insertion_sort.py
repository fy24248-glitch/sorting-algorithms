def insertion_sort(arr):
    """Sorts a list in ascending order using Insertion Sort. O(n^2)."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11, 90, 5]
    print("Original:", sample)
    print("Sorted:  ", insertion_sort(sample))
