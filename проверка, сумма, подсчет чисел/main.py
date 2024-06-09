def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_array(arr):
    return sum(arr)

def count_positive_negative(arr):
    positive_count = sum(1 for x in arr if x > 0)
    negative_count = sum(1 for x in arr if x < 0)
    return positive_count, negative_count

def find_max_min(arr):
    max_num = max(arr)
    min_num = min(arr)
    return max_num, min_num

def main():
    # Задача 1: Проверка простого числа
    prime_numbers = [12, -45, 67, -34, 89, -100, 23, -5, 34]
    print("Проверка простых чисел:")
    for num in prime_numbers:
        print(f"{num}: {'Простое' if is_prime(num) else 'Не простое'}")
    print()

    # Задача 2: Сумма чисел в массиве
    sum_array = [-90, 56, -23, 12, 45, -67, 89, -32, 11, -76, 54]
    array_sum = sum_of_array(sum_array)
    print(f"Сумма чисел в массиве: {array_sum}")
    print()

    # Задача 3: Подсчет положительных и отрицательных чисел в массиве
    count_array = [3, -15, 27, -48, 59, -6, 14, -38, 72, -94, 18, -12]
    positive_count, negative_count = count_positive_negative(count_array)
    print(f"Положительных чисел: {positive_count}")
    print(f"Отрицательных чисел: {negative_count}")
    print()

    # Задача 4: Найти наибольшее и наименьшее число в массиве
    max_min_array = [-22, 45, -67, 34, -89, 100, -23, 5, -34, 78]
    max_num, min_num = find_max_min(max_min_array)
    print(f"Наибольшее число: {max_num}")
    print(f"Наименьшее число: {min_num}")

if __name__ == "__main__":
    main()
