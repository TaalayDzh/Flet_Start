import flet as ft


def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text('Hello World')
    name_input = ft.TextField(label='Введите имя:')

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)


        if name:
            greeting_text.value = f'Hello{name}'
            name_input.value = ''
        else:
            print('Ничего не введено')
            greeting_text.value = 'Пожалуйста введите имя'

        page.update()

    name_button = ft.ElevatedButton('SEND',icon=ft.Icons.SEND, on_click=on_button_click)
    # name_button_text = ft.TextButton('SEND')
    # name_button_icon = ft.TextButton(icon=ft.Icons.SEND)
    
    page.add(greeting_text,name_input, name_button)

ft.app(target=main)
