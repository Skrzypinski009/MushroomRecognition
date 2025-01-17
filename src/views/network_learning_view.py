from flet import *
import os
from controllers import NeuralNetwork
from controllers import train, scan_weights, make_plot
from time import sleep

cur_plot_nr = 0

def getImage(path):
    new_image = Image(path, width=500)
    return new_image

def get_list_from(layers_sizes: str) -> list|None:
    sizes_list = layers_sizes.split(',')
    result = []
    for size in sizes_list:
        try:
            result.append(int(size))
        except:
            return None
    return result


def network_learning_view(page) -> View:
    global selected_nn, weights_list
    selected_nn = None
    weights_list = scan_weights()

    view = View(route='/nl')
    
    h1_style = TextStyle(44)
    h2_style = TextStyle(24)
    error_style = TextStyle(20, color='red')
    button_style = ButtonStyle(text_style=h2_style)

    title = Text("Trenowanie sieci neuronowej", style=h1_style)
    title_row = Row([title], alignment='center')

    back_button = FilledTonalButton("<- Klasyfikacja", style=button_style)
    row1 = Row([back_button], alignment='center')

    layers_field = TextField(width=300, text_style=h2_style)
    row2 = Row([
        Text("Rozmiary ukrytych warstw rozdzielone ','", style=h2_style),
        layers_field,
    ], alignment='center')

    network_name_field = TextField(width=300, text_style=h2_style)
    row5 = Row([
        Text("Nazwa wag:", style=h2_style),
        network_name_field,
    ], alignment='center')

    create_button = FilledButton("Stwórz", style=ButtonStyle(text_style=h2_style), width=160, height=40)
    row7 = Row([create_button], alignment='center')

    error_message = Text("", style=error_style)
    row8 = Row([error_message], alignment='center')

    row9 = Row([Text("Albo wybierz istniejace", style=h2_style)], alignment='center')
    dropdown_weights = Dropdown(options=[], text_style=h2_style)
    row10 = Row([dropdown_weights], alignment='center')

    iterations = TextField('', text_style=h2_style, text_align='center', width=50)
    train_button = FilledTonalButton("Trenuj", style=ButtonStyle(text_style=h2_style), width=150, height=40)
    row11 = Row([ 
        Text('Iteracje ', style=h2_style), 
        iterations,
        train_button
    ], alignment='center')

    row12 = Row([], alignment='center')
    training_text = Text("Trenowanie...", visible=False)
    row13 = Row([training_text], alignment='center')

    pb = ProgressBar(0, color='white', width=500, visible=False)
    pb.value = 0
    row14 = Row([pb], alignment='center')

    result = Text("", style=h2_style)
    row15 = Row([result], alignment='center')

    view.controls = [Column([
        title_row,
        row1,
        row2,
        row5,
        row7,
        row8,
        row9,
        row10,
        row11,
        row12,
        row13,
        row14,
        row15
    ])]

    def nn_selected(e: ControlEvent) -> None:
        global selected_nn
        selected_nn = NeuralNetwork(file_path='data/weights/' + dropdown_weights.value)
        view.update()
        print_nn()
    
    def print_nn():
        global selected_nn
        print("nn wybrane: " + str(selected_nn))

    def train_pressed(e: ControlEvent) -> None:
        # sizes_list = get_list_from(layers_field.value)
        # if not sizes_list: error_message.value = "Layers sizes input is not correct"; return
        global selected_nn
        print(selected_nn)
        if not selected_nn: return
        print("good 1")
        try: int(iterations.value)
        except: return
        print("all good")

        training_text.visible=True
        pb.visible = True
        pb.value = 0
        result.visible = False
        row12.controls = []
        # if os.path.exists('data/plot.png'): os.remove('data/plot.png')
        view.update()
        training_wait()

    def training_wait():
        global selected_nn
        global cur_plot_nr
        cur_plot_nr += 1

        err_arr = train(selected_nn, int(iterations.value), cur_plot_nr, view)
        make_plot(err_arr['train'], 'data/train_err_plot' + str(cur_plot_nr) + '.png', "Błąd na danych treningowych")
        make_plot(err_arr['test'], 'data/test_err_plot' + str(cur_plot_nr) + '.png', "Błąd na danych testowych")

        training_text.visible = False
        pb.visible = False
        result.visible = True
        train_err_plot = 'data/train_err_plot' + str(cur_plot_nr) + '.png'
        test_err_plot = 'data/test_err_plot' + str(cur_plot_nr) + '.png'
        row12.controls.append(getImage(train_err_plot))
        row12.controls.append(getImage(test_err_plot))
        view.update()

    def create_pressed(e: ControlEvent):
        hidden_sizes = get_list_from(layers_field.value)
        if not hidden_sizes:
            error_message.value = "Nie poprawny rozmiar warstw"
            page.update()
            return
        sizes = [22] + hidden_sizes +[1]
        name = network_name_field.value.strip()
        NeuralNetwork(sizes, True).save_to_file('data/weights/' + name)
        refresh_dropdown()
        view.update()

    def refresh_dropdown():
        weights_list = scan_weights()
        dropdown_weights.options.clear()
        for option in [dropdown.Option(w_name) for w_name in weights_list]:
            dropdown_weights.options.append(option)


    refresh_dropdown()

    create_button.on_click=create_pressed
    dropdown_weights.on_change=nn_selected
    train_button.on_click = train_pressed
    back_button.on_click = lambda e: page.go('/')
    return view