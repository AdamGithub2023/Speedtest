import flet as ft
import speedtest
import time
a = 0
def main(page:ft.Page):
    page.title = "Speedtest"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 30
    page.window_bgcolor = "blue"
    page.bgcolor = "black"
    st = speedtest.Speedtest()
    page.fonts = {"Rooster": "RoosterPersonalUse-3z8d8.ttf", "Source1": "SourceCodePro-BlackItalic.ttf", "Source2":
        "SourceCodePro-Bold.ttf"}
    title = ft.Row(controls=[ft.Text(value="Speed", font_family="Rooster", style="displayLarge", color="Red"),
                             ft.Text(value="Test", font_family="Rooster", style="displayLarge", color="Yellow")],
                   alignment="center")
    line1 = ft.Text(value="Press Start...", font_family="Source1", color="White")
    line2 = ft.Text(value="", font_family="Source1", color="Yellow")
    line3 = ft.Text(value="", font_family="Source1", color="Yellow")
    bar1 = ft.ProgressBar(width=400, color="blue", opacity=0)
    bar_text1 = ft.Text(value=" ", font_family="Source1", color="Yellow")
    progess_row1 = ft.Row([bar_text1, bar1])
    line4 = ft.Text(value="", font_family="Source2", color="Green")
    line5 = ft.Text(value="", font_family="Source1", color="Yellow")
    line6 = ft.Text(value="", font_family="Source1", color="Yellow")
    bar2 = ft.ProgressBar(width=400, color="blue", opacity=0)
    bar_text2 = ft.Text(value=" ", font_family="Source1", color="Yellow")
    progess_row2 = ft.Row([bar_text2, bar2])
    line7 = ft.Text(value="", font_family="Source1", color="Green")
    line8 = ft.Text(value="", font_family="Source2", color="White")
    col_text = ft.Column([line1, line2, line3, progess_row1, line4, line5, line6, progess_row2, line7, line8])
    speedcon = ft.Container(
        content=col_text,
        width=200,
        height=100,
        bgcolor="grey",
        border_radius=30,
        padding=20,
        animate=ft.animation.Animation(1000, "bounceOut")
    )

    def btn(event):
        progess_row1.opacity = 0
        bar1.opacity = 0
        bar1.value = None
        progess_row2.opacity = 0
        bar2.opacity = 0
        bar2.value = None
        line1.update()
        line2.update()
        line3.update()
        line4.update()
        line5.update()
        line6.update()
        line7.update()
        line8.update()
        speedcon.update()
        speedcon.width = 700
        speedcon.height = 400
        line1.value = "> calculating download, please wait..."
        speedcon.update()
        time.sleep(1)
        line1.update()
        best_s = st.get_best_server()
        city = best_s["name"]
        country = best_s["country"]
        cc = best_s["cc"]
        line2.value = f"> finding the best possible servers in {city}, {country}, {cc}"
        line2.update()
        speedcon.update()
        time.sleep(1)
        line3.value = "> connection established, status OK, fetching download speed"
        line3.update()
        progess_row1.opacity = 1
        bar1.opacity = 1
        speedcon.update()
        ds = st.download()/1024/1024
        bar1.value = 1
        line4.value = f"> the download is {str(round(ds,2))}Mbps"
        line4.update()
        speedcon.update()
        line5.value = "> calculating upload speed, please wait..."
        line5.update()
        speedcon.update()
        time.sleep(1)
        line6.value = "> executing upload script, hold on"
        line6.update()
        progess_row2.opacity = 1
        bar2.opacity = 1
        speedcon.update()
        us = st.upload()/1024/1024
        bar2.value = 1
        line7.value = f"> the upload is {str(round(us,2))}Mbps"
        line7.update()
        speedcon.update()
        line8.value = "Task completed successfully"
        line8.update()
        speedcon.update()


    page.add(title, speedcon, ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=btn, icon_color="green", icon_size=50))


ft.app(target=main, assets_dir="asset")