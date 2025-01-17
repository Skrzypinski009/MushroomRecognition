import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
import json
import requests
import os
import zipfile
import time
from flet import View

from . import NeuralNetwork
import data
from data import encoding


def download_dataset(save_path):
    r = requests.get('https://archive.ics.uci.edu/static/public/73/mushroom.zip', stream=True)
    if not r: return False

    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    with open('tmp/dataset.zip', 'wb') as fd:
        for chunk in r.iter_content(256):
            fd.write(chunk)
        fd.close()
    
    with zipfile.ZipFile('tmp/dataset.zip', 'r') as zipf:
        zipf.extract("agaricus-lepiota.data", "data/")
    
    os.rename("data/agaricus-lepiota.data", "data/dataset.csv")

    os.remove('tmp/dataset.zip')
    os.rmdir("tmp")
    return True
#end

def download_dataset_with_check(save_path):
    if not is_dataset_present(save_path):
        print("The dataset does not exist")
        try:
            requests.get('https://www.google.com')
        except:
            print("There is no internet connection to download the dataset")
            return False
        print("Downloading the dataset...")
        good = download_dataset(save_path)
        if not good:
            print("Error while downloading the dataset")
            return False
    print("The dataset is ready to use")
    
#end

#lambda function
is_dataset_present = lambda path: os.path.exists(path)

#lambda function
get_dataset_from_csv = lambda path: pd.read_csv(path, names=data.columns)

def get_dataset_from_uci():
    mushroom = fetch_ucirepo(id=73)
    return pd.merge( mushroom.data.features,
                     mushroom.data.targets,
                     left_index=True,
                     right_index=True)
#end

#lambda function
def get_merged(dataset):
    dataset.drop_duplicates()
    dataset.replace({'stalk-root': [np.nan]}, {'stalk-root': ['?']}, inplace=True)
    return dataset.sample(frac = 1, random_state=0)
    # return dataset
#end

def get_numerical_data(categorical_data: pd.DataFrame) -> pd.DataFrame:
    numerical_data = categorical_data.copy()
    col_names = numerical_data.columns

    for col in col_names:
        categorical = list(encoding[col].keys())
        numeric = list(encoding[col].values())

        numerical_data.replace({col: categorical}, {col: numeric}, inplace=True)
    return numerical_data.astype('int32')
#end

def xy_data(numerical_data: pd.DataFrame) -> list[pd.DataFrame, pd.Series]:
    x = numerical_data
    y = x.pop('poisonous')
    return x, y
#end

def get_training_and_testing_data(
    data_x: pd.DataFrame, data_y: pd.Series, fraction: float
    ) -> list[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:

    training_size = int(data_x.shape[0] * fraction)

    train_data = data_x.iloc[:training_size]
    train_y = data_y.iloc[:training_size]

    test_data = data_x.iloc[training_size:]
    test_y = data_y.iloc[training_size:]

    return (train_data, train_y, test_data, test_y)
#end

def train_NN(
    nn: NeuralNetwork,
    training_data: pd.DataFrame, training_y: pd.Series,
    testing_data: pd.DataFrame, testing_y: pd.Series,
    iterations: int, accuracy: float, err_arr: dict, view: View) -> list:


    i = 0
    for i in range(iterations):
        dd = []
        ee = []
        for j in range(training_data.shape[0]):
            nn.forwardsPropagation(training_data.iloc[j])
            d = nn.get_error(training_y.iloc[j])
            dd.append(d)
            nn.backwardsPropagation([training_y.iloc[j]])
        for j in range(testing_data.shape[0]):
            nn.forwardsPropagation(testing_data.iloc[j])
            e = nn.get_error(testing_y.iloc[j])
            ee.append(e)

        err_arr['train'].append(np.sum(dd))
        err_arr['test'].append(np.sum(ee))

        view.controls[0].controls[11].controls[0].value = (i+1) / iterations
        view.update()

        if(np.sum(dd) < 0.000003):
            print(f"brakeing at: {i+1} iteration")
            break
#end

def make_plot(err_arr: list, save_path: str, title: str = "") -> None:
    plt.clf()
    x = np.arange(1,len(err_arr)+1,1)
    plt.xlabel("Iterations")
    plt.ylabel("Error")
    plt.title(title)
    plt.plot(x, err_arr, c="black", lw="2" )
    plt.savefig(save_path)
    plt.close()
#end

def get_ready_data() -> list:
    dataset = get_dataset_from_csv('data/dataset.csv')
    merged = get_merged(dataset)
    numerical = get_numerical_data(merged)
    x, y = xy_data(numerical)
    return get_training_and_testing_data(x, y, 0.7)
#end

def train(nn: NeuralNetwork, iterations: int, plot_nr: int, view: View) -> None:
    (train_features,
    train_target,
    test_fretures,
    test_target) = get_ready_data()

    err_arr = {'train': [], 'test': []}
    train_NN(
        nn,
        train_features, train_target,
        test_fretures, test_target,
        iterations, 10, err_arr, view)
    view.controls[0].controls[12].controls[0].value = "Effectiveness: " + str(get_correct_results(nn, test_fretures, test_target)['procentage']) + "%"
    return err_arr
#end

def scan_weights() -> list:
    weights_list = []
    for file in os.listdir('data/weights/'):
        weights_list.append(file)
    return weights_list
#end


def get_correct_results(nn: NeuralNetwork, testing_data: pd.DataFrame, testing_y: pd.Series) -> dict:
    correct = 0
    for j in range(testing_data.shape[0]):
        nn.forwardsPropagation(testing_data.iloc[j])
        s = 1 if nn.neurons[-1] > 0.5 else 0
        if s == testing_y.iloc[j]:
            correct += 1
    return {
        'procentage': correct / testing_data.shape[0] * 100,
        'count': correct,
        'all': testing_data.shape[0]}
