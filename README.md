# Mushroom Recognition

UI app for running neural network, that is predicting whether a  mushroom with given characterictics is poisonous or edible. <br>

This project is licensed under the terms of the MIT license. <br>

### Used Tehnology
- **Python**
- **[Flet](https://flet.dev/)** <br>
    Python library that is build with [Flutter](https://flutter.dev/)
- **Git with Github**


## Files description

### src/data
- **variable_data.py:** <br>
    Encoding of dataset characteristics.
- **weights.txt** <br>
    Weights saved from NeuralNetwork. 
### src/views
- **classification_view.py:** <br>
    Page, that allows for choose features of mushroom and check if it would be poisonous or not.
- **network_learning_view.py** <br>
    Page made for training new NeuralNetwork and create new weights file.
### src/controllers
- **neural_network.py:** <br>
    Contains the NeuralNetwork class, that allow for creating NN, with layer sizes of your choice, train it, save and load from file and others.
- **network_training.py** <br>
    Set of funcitons for transforming the data and training NeuralNetwork.
    


## Usefull commands

- creating virtual envirement (venv): <br>
    ```python -m venv <venv_name>```

- run venv:<br>
    - Linux: <br>
        ```source <venv_name>/bin/activate```<br> 
    - Windows: <br>
        ```<venv_name>\Scripts\activate.bat```

- libraries installation (requires python package manager "pip"): <br>
    ```pip install -r requirements.txt```

 - run app: <br>
    ```python app.py```

