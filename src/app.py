from flet import *
import requests

from views import classification_view
from views import network_learning_view
from controllers import download_dataset_with_check

def main(page: Page):
    page.title = 'Rozpoznawanie Grzybów'
    page.theme_mode = 'dark'
    page.window.width = 400
    page.window.height = 600

    def route_change(e: RouteChangeEvent):
        page.views.clear()

        if page.route == '/':
            page.views.append(
                classification_view(page),
            )
        elif page.route == '/nl':
            page.views.append(
                network_learning_view(page),
            )
        page.update()

    def view_pop(e: ViewPopEvent):
        page.views.pop()
        top_veiw = page.views[-1]
        page.go(top_veiw.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go('/')

if __name__ == "__main__":
    download_dataset_with_check('data/dataset.csv')

    app(target=main)