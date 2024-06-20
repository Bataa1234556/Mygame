import flet as ft
from page2 import LoginPage as LG

class HoverableImage:
    def __init__(self, path, width, height):
        self.image = ft.Image(path, width=width, height=height)
        self.original_scale = (1.0, 1.0)
        self.hover_scale = (1.1, 1.1)
        self.image.mouse_enter = self.on_mouse_enter
        self.image.mouse_leave = self.on_mouse_leave
        self.is_hovered = False

    def on_mouse_enter(self, e):
        if not self.is_hovered:
            self.is_hovered = True
            self.image.animate([
                ft.Animation.ease_in_out(duration=0.3, scale=self.hover_scale)
            ])

    def on_mouse_leave(self, e):
        if self.is_hovered:
            self.is_hovered = False
            self.image.animate([
                ft.Animation.ease_in_out(duration=0.3, scale=self.original_scale)
            ])

def main(page: ft.Page):
    def route_change(route):
        page.clean()
        if route.route == "/":
            show_main_page(page)
        elif route.route == "/LG":
            LG(page)
        page.update()

    def show_main_page(page: ft.Page):
        page.title = "Word Find Game"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor = ft.colors.WHITE

        # Top gray empty space
        top_empty_space = ft.Container(height=page.window.height * 0.1, bgcolor=ft.colors.LIGHT_BLUE)

        logo_path = r'C:\Users\user\Documents\game\image1-removebg-preview.png'
        hoverable_logo = HoverableImage(logo_path, width=300, height=200)

        # Add shadow to hoverable_logo
        hoverable_logo_container = ft.Container(
            content=hoverable_logo.image,
            shadow=ft.BoxShadow(
                blur_radius=10,
                color=ft.colors.BLACK,
                spread_radius=2,
                offset=ft.Offset(2, 2)
            ),
            padding=ft.padding.all(20),
            border_radius=ft.border_radius.all(10),
        )

        # Start Game button
        start_button = ft.ElevatedButton(text="Start Game", on_click=lambda e: page.go("/LG"))

        # Page layout
        page.add(
            top_empty_space,
            ft.Column(
                [
                    ft.Row([hoverable_logo_container], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([start_button], alignment=ft.MainAxisAlignment.CENTER),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    page.on_route_change = route_change
    page.go("/")  # Set the initial route to the main page

ft.app(target=main)
