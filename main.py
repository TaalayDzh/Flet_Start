import flet as ft


def main(page: ft.Page):
    page.title = 'Мое первое приложение!'

    greeting_text = ft.Text('Hello World')

    page.add(greeting_text)

ft.app(target=main)
