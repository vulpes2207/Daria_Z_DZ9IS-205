def find_division_index(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == 0:
            left = mid + 1
        else:
            right = mid - 1

    if left < len(arr) and arr[left] == 1:
        return left
    else:
        return -1

def main():
    try:
        array = list(map(int, input("Введите упорядоченный массив из 0 и 1 через запятую (например, 0,0,0,1,1): ").split(',')))
        index = find_division_index(array)
        if index != -1:
            print(f"Место разделения: Индекс {index}")
        else:
            print("Разделение не найдено")
    except ValueError:
        print("Ошибка: введите корректный массив из 0 и 1, разделенных запятыми.")

if __name__ == "__main__":
    main()
