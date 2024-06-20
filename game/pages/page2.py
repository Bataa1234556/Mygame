import flet as ft

def LoginPage(page: ft.Page):
    page.title = "Login Page"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    # Create the login page content
    login_form = ft.Column(
        [
            ft.Text("Login Page", style="headlineMedium"),
            ft.TextField(label="Username"),
            ft.TextField(label="Password", password=True),
            ft.ElevatedButton(text="Login", on_click=lambda e: page.go("/"))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(login_form)
