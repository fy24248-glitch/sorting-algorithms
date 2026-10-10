def bubble_sort(arr):
    """Sorts a list in ascending order using Bubble Sort. O(n^2)."""
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11, 90, 5]
    print("Original:", sample)
    print("Sorted:  ", bubble_sort(sample))
