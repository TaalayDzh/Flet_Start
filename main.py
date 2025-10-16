import flet as ft
from datetime import datetime
import re  # для извлечения имени из строки

def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text('Hello World', selectable=True)
    age_input = ft.TextField(label='Введите возраст:', expand=True)
    
    greeting_history = []
    history_text = ft.Text('История приветствий:')

    # функция генерации приветствия
    def get_greeting(name, age):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            greeting = "Доброе утро, "
        elif 12 <= hour < 18:
            greeting = "Добрый день, "
        elif 18 <= hour < 24:
            greeting = "Добрый вечер, "
        else:
            greeting = "Доброй ночи, "

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        # Возвращаем форматированный текст (без ft.Text, просто строку)
        return f"{current_time} - {greeting}{name}! Тебе {age} лет."

    def update_history_text():
        """Обновляем текст истории приветствий"""
        if greeting_history:
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)
        else:
            history_text.value = 'История приветствий: (пусто)'

    def extract_name(entry: str):
        """Извлекает имя из строки истории"""
        match = re.search(r",\s*([А-ЯA-ZЁ][а-яa-zё]+)!", entry)
        return match.group(1) if match else ""

    def on_button_click(_):
        name = name_input.value.strip()
        age = age_input.value.strip()

        if not name:
            greeting_text.value = 'Пожалуйста, введите имя!'
            greeting_text.spans = []
        elif not age:
            greeting_text.value = 'Введите возраст!'
            greeting_text.spans = []
        else:
            # создаём строку приветствия
            greeting = get_greeting(name, age)
            # форматированный вывод с цветным именем
            greeting_text.value = None  # очищаем обычное значение
            greeting_text.spans = [
                ft.TextSpan(greeting.split(name + "!")[0]),
                ft.TextSpan(f"{name}!", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                ft.TextSpan(greeting.split(name + "!")[1])
            ]
            # добавляем в историю
            greeting_history.append(greeting)
            update_history_text()

            # очищаем поля
            name_input.value = ''
            age_input.value = ''
        page.update()

    def on_clear_click(_):
        greeting_text.value = 'Hello World'
        greeting_text.spans = []
        greeting_history.clear()
        update_history_text()
        name_input.value = ''
        age_input.value = ''
        page.update()

    def on_delete_last_click(_):
        if greeting_history:
            greeting_history.pop()
            update_history_text()
        else:
            greeting_text.value = 'История пуста!'
            greeting_text.spans = []
        page.update()

    def on_sort_click(_):
        if greeting_history:
            greeting_history.sort(key=lambda x: extract_name(x).lower())
            update_history_text()
        else:
            greeting_text.value = 'История пуста!'
            greeting_text.spans = []
        page.update()

    # элементы интерфейса
    name_input = ft.TextField(label='Введите имя:', on_submit=on_button_click)
    name_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    delete_last_button = ft.IconButton(icon=ft.Icons.REMOVE_CIRCLE_OUTLINE, tooltip="Удалить последнее", on_click=on_delete_last_click)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, tooltip="Очистить всё", on_click=on_clear_click)
    sort_button = ft.IconButton(icon=ft.Icons.SORT_BY_ALPHA, tooltip="Сортировать по алфавиту", on_click=on_sort_click)

    page.add(
        greeting_text,
        name_input,
        age_input,
        ft.Row(
            [name_button, delete_last_button, clear_button, sort_button],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),
        history_text
    )

ft.app(target=main)

