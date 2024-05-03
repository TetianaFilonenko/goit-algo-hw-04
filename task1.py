import timeit
import random


def insertion_sort(arr):
    """Implementation of the insertion sort algorithm"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    """Implementation of the merge sort algorithm"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def compare_sorting_algorithms():
    """Function to compare the efficiency of algorithms"""
    local_sizes = [1000, 2000, 5000, 10000]
    local_results = {"Insertion Sort": [], "Merge Sort": [], "Timsort": []}
    for size in local_sizes:
        array = [random.randint(0, 100000) for _ in range(size)]
        local_results["Insertion Sort"].append(
            timeit.timeit(
                "insertion_sort(arr.copy())",
                globals=globals(),
                number=1,
                setup=f"arr={array}",
            )
        )
        local_results["Merge Sort"].append(
            timeit.timeit(
                "merge_sort(arr.copy())",
                globals=globals(),
                number=1,
                setup=f"arr={array}",
            )
        )
        local_results["Timsort"].append(
            timeit.timeit(
                "sorted(arr)", globals=globals(), number=1, setup=f"arr={array}"
            )
        )
    return local_results, local_sizes


# Run the comparison of algorithms
results, sizes = compare_sorting_algorithms()

# Display the header
print(
    f"| {'Size':>10} | {'Insertion Sort':>15} | {'Merge Sort':>10} | {'Timsort':>8} |"
)

# Print the rows
for i, size in enumerate(sizes):
    print(
        f"| {size:>10} | {results['Insertion Sort'][i]:>15.5f} | {results['Merge Sort'][i]:>10.5f} | {results['Timsort'][i]:>8.5f} |"
    )
