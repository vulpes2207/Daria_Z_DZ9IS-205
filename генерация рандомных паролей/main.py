import random
import string


def generate_password(length, use_digits, use_symbols, use_uppercase):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Нужно выбрать хотя бы один тип символов для генерации пароля.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_unique_passwords(count, length, use_digits, use_symbols, use_uppercase):
    passwords = set()
    while len(passwords) < count:
        password = generate_password(length, use_digits, use_symbols, use_uppercase)
        passwords.add(password)
    return list(passwords)


def main():
    try:
        length = int(input("Введите длину пароля: "))
        use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
        use_symbols = input("Использовать символы? (y/n): ").lower() == 'y'
        use_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'

        passwords = generate_unique_passwords(5, length, use_digits, use_symbols, use_uppercase)

        print("\nСгенерированные пароли:")
        for password in passwords:
            print(password)
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
