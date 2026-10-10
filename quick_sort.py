def quick_sort(arr):
    """Sorts a list in ascending order using Quick Sort. Average O(n log n)."""
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11, 90, 5]
    print("Original:", sample)
    print("Sorted:  ", quick_sort(sample))
