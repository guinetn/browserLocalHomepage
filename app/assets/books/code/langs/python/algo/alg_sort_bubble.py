def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def make_random_array():
    from random import randint

    return [randint(-100, 100) for i in range(20)]

if __name__ == "__main__":

	unsorted_array = make_random_array()
	print(f"Unsorted: {unsorted_array}")

	sorted_array = bubble_sort(unsorted_array)
	print(f"Sorted: {sorted_array}")