from flet import *
from random import randint

from controllers import NeuralNetwork
from data import variable_data, encoding
from controllers import scan_weights

def classification_view(page: Page) -> View:
    global selected_nn
    selected_nn = NeuralNetwork(file_path='data/weights/weights.txt')

    view = View('/')
    title_control = Container(
        Text("Mushroom Recognition", size=40), margin=40
    )

    button_style = ButtonStyle(text_style=TextStyle(size=25))

    weights = Dropdown(
        options = [dropdown.Option(w_name) for w_name in scan_weights()],
        text_style=TextStyle(25),
        value='weights.txt'
    )
    nt_button = FilledTonalButton("Network training ->", style=button_style)

    button_random = Container(FilledTonalButton("Randomize", 
        style=button_style, width=200, height=50
    ), margin=30)

    button_submit = Container(FilledTonalButton("Submit", 
        style=button_style, width=200, height=50
    ), margin=30)


    image_skull = Image('data/resources/skull.png', height=150 ,width=300)
    image_smile = Image('data/resources/laughing.png', height=150, width=300)
    popup = AlertDialog(
        title=Text("Popup test"),
        actions=[
            TextButton("Close", on_click=lambda e: page.close(popup))
        ],
    )


    # ADDING 
    rows_controlls = []
    rows_controlls.append(Row(controls=[title_control], alignment=MainAxisAlignment.CENTER))
    rows_controlls.append(Row([weights, nt_button], alignment='center'))

    columns = []
    for i in range(0,2):
        rows = []
        for j in range(0, 11):
            idx = 11 * i + j
            options = [ dropdown.Option(option) for option in variable_data[idx]['options'] ]
            rows.append(Row(controls=[
                Text(variable_data[idx]['name'], size=25, width=300),
                Dropdown(options=options, width=200),
            ]))
        columns.append(Column(rows))
    rows_controlls.append(Row(controls=columns, spacing=100, alignment=MainAxisAlignment.CENTER))
    
    rows_controlls.append(Row(
        controls=[button_random, button_submit],
        alignment=MainAxisAlignment.CENTER,
        spacing=50
    ))

    def random_values(e: ControlEvent) -> None:
        for i in range(0, 2):
            for j in range(0, 11):
                dropdown_variable = columns[i].controls[j].controls[1]
                option_size = len(dropdown_variable.options)
                rand_int = randint(0, option_size-1)
                try:
                    rand_option: dropdown.Option = dropdown_variable.options[rand_int]
                except:
                    print(f"Index {rand_int} out of range")
                dropdown_variable.value = rand_option.key
        page.update()
    
    def predict(e: ControlEvent) -> None:
        values = []
        for i in range(0, 2):
            for j in range(0, 11):       
                idx = 11 * i + j
                variable_name = variable_data[idx]['name']
                variable_value = columns[i].controls[j].controls[1].value
                half_encoded_value = variable_data[idx]['options'][variable_value]
                encoded_value = encoding[variable_name][half_encoded_value]
                values.append(encoded_value)
        selected_nn.forwardsPropagation(values)
        s = 1 if selected_nn.neurons[-1] > 0.5 else 0
        message = "This looks like it could kill you mate." if s == 1 else "I think you can eat this"
        popup.title=Text(message)
        popup.content = image_skull if s == 1 else image_smile
        page.open(popup)

    def nn_selected(e: ControlEvent) -> None:
        global selected_nn
        selected_nn = NeuralNetwork(file_path='data/weights/' + weights.value)
        
    button_random.content.on_click = random_values
    button_submit.content.on_click = predict
    weights.on_change = nn_selected

    view.controls = rows_controlls
    nt_button.on_click = lambda e: page.go('/nl')
    return view
