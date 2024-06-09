import random


class QuestionManager:
    def __init__(self):
        self.questions = []

    def add_question(self):
        question = input("Введите вопрос: ")
        if question:
            self.questions.append(question)
            print("Вопрос добавлен.")
        else:
            print("Вопрос не может быть пустым.")

    def edit_question(self):
        self.show_questions()
        try:
            index = int(input("Введите номер вопроса для редактирования: ")) - 1
            if 0 <= index < len(self.questions):
                new_question = input("Введите новый текст вопроса: ")
                if new_question:
                    self.questions[index] = new_question
                    print("Вопрос обновлен.")
                else:
                    print("Вопрос не может быть пустым.")
            else:
                print("Неверный номер вопроса.")
        except ValueError:
            print("Неверный ввод, пожалуйста введите номер вопроса.")

    def delete_question(self):
        self.show_questions()
        try:
            index = int(input("Введите номер вопроса для удаления: ")) - 1
            if 0 <= index < len(self.questions):
                del self.questions[index]
                print("Вопрос удален.")
            else:
                print("Неверный номер вопроса.")
        except ValueError:
            print("Неверный ввод, пожалуйста введите номер вопроса.")

    def show_questions(self):
        if self.questions:
            print("\nСписок вопросов:")
            for i, question in enumerate(self.questions, 1):
                print(f"{i}. {question}")
        else:
            print("Список вопросов пуст.")

    def ask_random_question(self):
        if self.questions:
            question = random.choice(self.questions)
            print(f"\nСлучайный вопрос: {question}")
        else:
            print("Список вопросов пуст.")


def main():
    manager = QuestionManager()
    while True:
        print("\nМеню:")
        print("1. Добавить вопрос")
        print("2. Редактировать вопрос")
        print("3. Удалить вопрос")
        print("4. Показать все вопросы")
        print("5. Задать случайный вопрос")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            manager.add_question()
        elif choice == '2':
            manager.edit_question()
        elif choice == '3':
            manager.delete_question()
        elif choice == '4':
            manager.show_questions()
        elif choice == '5':
            manager.ask_random_question()
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
