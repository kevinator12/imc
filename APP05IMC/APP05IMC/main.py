import flet as ft
from cProfile import label


def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor="green"
    
    txtpeso=ft.TextField(label="ingresa tu peso")
    txtaltura=ft.TextField(label="ingresa la altura")
    lbl=ft.Text("tu IMC es: ")
    
    img=ft.Image(src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
                width=200,
                height=200
                
                )
    btnCalcular=ft.ElevatedButton(text="Calcular")
    btnLimpiar=ft.ElevatedButton(text="Limpiar")
    
    page.add(
        ft.Column(
            controls=[txtpeso, 
                    txtaltura, 
                    lbl
                    ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                    btnCalcular,
                    btnLimpiar
            ],alignment="CENTER")
    )


ft.app(target=main,view=ft.AppView.WEB_BROWSER)
