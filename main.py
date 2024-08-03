from Django_tasks_logika.django_tasks_git_start import User, Task


def create_user(name):
    user = User(name=name)
    user.save()
    print(f"Користувач {name} створений")


def create_task(title, description, status='in_progress', assigned_to=None):
    if assigned_to:
        try:
            assigned_user = User.objects.get(id=assigned_to)
        except User.DoesNotExist:
            print(f"Користувач з id {assigned_to} не знайдено")
            return
    else:
        assigned_user = None

    task = Task(title=title, description=description, status=status, assigned_to=assigned_user)
    task.save()
    print(f"Завдання '{title}' створено")


def assign_task(task_id, user_id):
    try:
        task = Task.objects.get(id=task_id)
        user = User.objects.get(id=user_id)
        task.assigned_to = user
        task.save()
        print(f"Завдання '{task.title}' призначено користувачу {user.name}")
    except Task.DoesNotExist:
        print(f"Завдання з id {task_id} не знайдено")
    except User.DoesNotExist:
        print(f"Користувач з id {user_id} не знайдено")


def change_task_status(task_id, new_status):
    try:
        task = Task.objects.get(id=task_id)
        if new_status in dict(Task.STATUS_CHOICES).keys():
            task.status = new_status
            task.save()
            print(f"Статус завдання '{task.title}' змінено на {new_status}")
        else:
            print("Неправильний статус")
    except Task.DoesNotExist:
        print(f"Завдання з id {task_id} не знайдено")


def list_tasks():
    tasks = Task.objects.all()
    if not tasks:
        print("Завдань не знайдено")
    else:
        for task in tasks:
            assigned_user = task.assigned_to.name if task.assigned_to else "Не призначено"
            print(
                f"ID: {task.id}, Назва: {task.title}, Опис: {task.description}, Статус: {task.get_status_display()}, Призначено: {assigned_user}")


def menu():
    while True:
        print("\nМеню:")
        print("1. Створити користувача")
        print("2. Створити завдання")
        print("3. Призначити завдання користувачу")
        print("4. Змінити статус завдання")
        print("5. Переглянути всі завдання")
        print("6. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я користувача: ")
            create_user(name)
        elif choice == '2':
            title = input("Введіть назву завдання: ")
            description = input("Введіть опис завдання: ")
            status = input("Введіть статус (in_progress, completed, postponed): ")
            assigned_to = input("Введіть id користувача для призначення (залиште порожнім, якщо не потрібно): ")
            assigned_to = int(assigned_to) if assigned_to else None
            create_task(title, description, status, assigned_to)
        elif choice == '3':
            task_id = input("Введіть id завдання: ")
            user_id = input("Введіть id користувача: ")
            assign_task(int(task_id), int(user_id))
        elif choice == '4':
            task_id = input("Введіть id завдання: ")
            new_status = input("Введіть новий статус (in_progress, completed, postponed): ")
            change_task_status(int(task_id), new_status)
        elif choice == '5':
            list_tasks()
        elif choice == '6':
            break
        else:
            print("Неправильний вибір, спробуйте ще раз")


if __name__ == "__main__":
    menu()