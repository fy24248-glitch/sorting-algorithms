from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

sample = [64, 25, 12, 22, 11, 90, 5]

print("Original array:", sample)
print("Bubble Sort:   ", bubble_sort(sample))
print("Selection Sort:", selection_sort(sample))
print("Insertion Sort:", insertion_sort(sample))
print("Merge Sort:    ", merge_sort(sample))
print("Quick Sort:    ", quick_sort(sample))
