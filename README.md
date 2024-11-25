# Mushroom Recognition

UI app for running neural network, that is predicting whether a  mushroom with given characterictics is poisonous or edible. <br>

This project is licensed under the terms of the MIT license. <br>


## Files description

- **neural_network.py:** <br>
    Contains the NeuralNetwork class, that allow for creating NN, with layer sizes of your choice, train it, save and load from file and others.
- **main.py:** <br>
    The flet main page, that takes care of running the app, creating all of the UI elements and using neural_network module for integration with NN.
- **variable_data.py:** <br>
    File that contains encoding of dataset characteristics.

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
    ```python main.py```

