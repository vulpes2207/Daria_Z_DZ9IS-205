class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self):
        item_name = input("Введите название предмета: ")
        if item_name in self.inventory:
            print("Этот предмет уже существует в инвентаре.")
            return
        item_description = input("Введите описание предмета: ")
        self.inventory[item_name] = item_description
        print("Предмет добавлен в инвентарь.")

    def delete_item(self):
        item_name = input("Введите название предмета для удаления: ")
        if item_name in self.inventory:
            del self.inventory[item_name]
            print("Предмет удален из инвентаря.")
        else:
            print("Такого предмета нет в инвентаре.")

    def view_item(self):
        item_name = input("Введите название предмета для просмотра: ")
        if item_name in self.inventory:
            print(f"Описание предмета '{item_name}': {self.inventory[item_name]}")
        else:
            print("Такого предмета нет в инвентаре.")

    def show_inventory(self):
        if self.inventory:
            print("\nСписок предметов в инвентаре:")
            for item_name, item_description in self.inventory.items():
                print(f"{item_name}: {item_description}")
        else:
            print("Инвентарь пуст.")


def main():
    manager = InventoryManager()
    while True:
        print("\nМеню:")
        print("1. Добавить предмет")
        print("2. Удалить предмет")
        print("3. Просмотреть предмет")
        print("4. Показать весь инвентарь")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            manager.add_item()
        elif choice == '2':
            manager.delete_item()
        elif choice == '3':
            manager.view_item()
        elif choice == '4':
            manager.show_inventory()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
