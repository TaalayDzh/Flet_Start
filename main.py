import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text('Hello World')
    name_input = ft.TextField(label='Введите имя:')
    age_input = ft.TextField(label='Введите возраст:', width=150)

    def get_greeting(name, age):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            greeting = f"Доброе утро, {name}!"
        elif 12 <= hour < 18:
            greeting = f"Добрый день, {name}!"
        elif 18 <= hour < 24:
            greeting = f"Добрый вечер, {name}!"
        else:
            greeting = f"Доброй ночи, {name}!"
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        return f"{current_time} - {greeting} Тебе {age} лет."

    def on_button_click(_):
        name = name_input.value.strip()
        age = age_input.value.strip()

        if not name:
            greeting_text.value = 'Пожалуйста, введите имя!'
        elif not age:
            greeting_text.value = 'Введите возраст!'
        else:
            greeting_text.value = get_greeting(name, age)
            name_input.value = ''
            age_input.value = ''
        
        page.update()

    name_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    
    page.add(
        greeting_text,
        name_input,
        age_input,
        name_button
    )

ft.app(target=main)
