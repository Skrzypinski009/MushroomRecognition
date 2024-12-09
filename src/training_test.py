from controllers import *

if __name__ == "__main__":
    (train_features,
    train_target,
    test_fretures,
    test_target) = get_ready_data()

    nn = NeuralNetwork([ 22, 16, 8, 1 ])
    err_arr = []
    train_NN(nn, train_features, train_target, 3, 10, err_arr)
    print(err_arr)
    make_plot(err_arr, 'data/plot.png')