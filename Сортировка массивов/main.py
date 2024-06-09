import time

def read_array_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
        if content.startswith('[') and content.endswith(']'):
            content = content[1:-1]
        array = list(map(int, content.split(',')))
    return array

# Пузырьковая сортировка (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Сортировка вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Сортировка слиянием (Merge Sort)
def merge_sort(arr):
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

# Быстрая сортировка (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Сортировка подсчетом (Counting Sort)
def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1

    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1

# Измерение времени выполнения
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

def main():
    file_path = 'mas-1.txt'
    array = read_array_from_file(file_path)

    # Пузырьковая сортировка
    array_copy = array[:]
    bubble_time = measure_time(bubble_sort, array_copy)

    # Сортировка вставками
    array_copy = array[:]
    insertion_time = measure_time(insertion_sort, array_copy)

    # Сортировка слиянием
    array_copy = array[:]
    merge_time = measure_time(merge_sort, array_copy)

    # Быстрая сортировка
    array_copy = array[:]
    quick_time = measure_time(lambda arr: quick_sort(arr), array_copy)

    # Сортировка подсчетом
    array_copy = array[:]
    counting_time = measure_time(counting_sort, array_copy)

    print(f"Сортировка пузырьком: {bubble_time:.6f} seconds")
    print(f"Сортировка вставками: {insertion_time:.6f} seconds")
    print(f"Сортировка слиянием: {merge_time:.6f} seconds")
    print(f"Быстрая сортировка: {quick_time:.6f} seconds")
    print(f"Сортировка подсчетом: {counting_time:.6f} seconds")



if __name__ == "__main__":
    main()
