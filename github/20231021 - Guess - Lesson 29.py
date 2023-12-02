import flet as ft
from random import randint

def main(page:ft.Page):
    page.title = "Guess the number"
    answer = randint(1, 100)
    page.fonts = {"SpaceMission": "asset/SpaceMission-rgyw9.otf", "Uncracked": "asset/Uncracked-X3WjK.otf"}
    player1 = ft.TextField(hint_text="Enter a number between 1-100: ", label="Player 1", border_radius=20)
    player2 = ft.TextField(hint_text="Enter a number between 1-100: ", label="Player 2", border_radius=20)
    ans = ft.Text(font_family="Uncracked", size=45)

    def check_1(event):
        if int(player1.value) < answer:
            ans.value = "Guess higher number"
        elif int(player1.value) > answer:
            ans.value = "Guess lower number"
        elif int(player1.value) == answer:
            ans.value = "You guessed it right"
        else:
            ans.value = "You should enter a number"
        page.update()

    def check_2(event):
        if int(player2.value) < answer:
            ans.value = "Guess higher number"
        elif int(player2.value) > answer:
            ans.value = "Guess lower number"
        elif int(player2.value) == answer:
            ans.value = "You guessed it right"
        else:
            ans.value = "You should enter a number"
        page.update()

    p1 = ft.ElevatedButton("Check", on_click=check_1)
    p2 = ft.ElevatedButton("Check", on_click=check_2)

    page.add(ft.Card(content=ft.Container(ft.Row(controls=[ft.Text(value="Guess the Number!", font_family="SpaceMission"
                                                                   , size=26, text_align="center")], alignment="center")
                                          , padding=20)), ft.Column(controls=[ft.Row([player1, p1]),
                                                                              ft.Row([player2, p2]),
                                                                              ans],
                                                                    horizontal_alignment="center"))


ft.app(target=main, assets_dir="asset")