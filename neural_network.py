import numpy as np
import pandas as pd

class NeuralNetwork:
    def __init__(self, layer_sizes=[], random_weights=True, file_path=""):
        if layer_sizes != []:
            self.create_from_layer_sizes(layer_sizes, random_weights)
        elif file_path != "":
            self.load_from_file(file_path)
    
    def create_from_layer_sizes(self, layer_sizes, random_weights):
        self.layer_sizes = np.array(layer_sizes)
        self.neurons = np.zeros(np.sum(self.layer_sizes))
        self.weights_sizes = np.multiply(
            self.layer_sizes[:-1], 
            self.layer_sizes[1:],
        )
        if random_weights:
            self.weights = self.get_random_weights()
        else:
            self.weights = np.zeros(np.sum(self.weights_sizes))
  
    def get_random_weights(self):
        return np.add(
            1,
            np.multiply(
                -2,
                np.random.rand(
                    np.sum(
                        self.weights_sizes
                    )
                )
            )
        )

    def load_from_file(self, file_path):
        with open(file_path, "r") as f:
            layer_sizes = f.readline()
            layer_sizes = layer_sizes.split(',')
            layer_sizes = [int(x) for x in layer_sizes]

            weights = f.readline()
            weights = weights.split(',')
            weights = np.array(weights).astype('float64')
            self.create_from_layer_sizes(layer_sizes, False)
            self.weights = weights

    def save_to_file(self, file_path):
        with open(file_path, "w") as f:
            for i, size in enumerate(self.layer_sizes):
                f.write(str(size))
                if i != len(self.layer_sizes) -1:
                    f.write(",");
            f.write("\n");
            for i, weight in enumerate(self.weights):
                f.write(str(weight))
                if i != len(self.weights) -1:
                    f.write(",");

    def printNeurons(self):
        idx = 0
        for i in self.layer_sizes:
            print("{", end='')
            for j in range(i):
                print(f"  {self.neurons[idx+j]}  ", end='')
            print("}")
            idx += i
        print("")

    def printWeights(self):
        idx = 0
        for i in range(len(self.weights_sizes)):
            w = self.weights_sizes[i]
            print("{", end='')
            for j in range(w):
                if j % self.layer_sizes[i] == 0:
                    print('')
                print(f"  {self.weights[idx+j]}  ", end='')
            print("\n}")
            idx+=i
        print("")

    def forwardsPropagation(self, inputs):
        for i, input in enumerate(inputs):
            self.neurons[i] = input

        S = np.zeros(np.sum(self.layer_sizes[1:]))

        index = 0
        w_index = 0
        for i in range(1, len(self.layer_sizes)):
            size = self.layer_sizes[i]
            
            for j in range(size):
                for w in range(0, self.layer_sizes[i-1]):
                    neuron_i = np.sum(self.layer_sizes[:i-1]) + w
                    S[index + j] += self.weights[w + w_index] * self.neurons[neuron_i]
                w_index += self.layer_sizes[i-1]
            
                self.neurons[np.sum(self.layer_sizes[:i]) + j] = 1/(1+np.exp(-S[index + j]))
            
            index += size

    def backwardsPropagation(self, outputs):
        d = np.zeros( np.sum( self.layer_sizes[1:] ) )
        index = len( self.neurons ) - 1
        w_index = len( self.weights ) -1
        
        for i in range( len( self.layer_sizes ) - 1 ):
            size = self.layer_sizes[ ::-1 ][i]
            prev_size = self.layer_sizes[ ::-1 ][ i+1 ]
            next_size = 0
            if i != 0:
                next_size = self.layer_sizes[ ::-1 ][ i-1 ]
            # print(f"size = {size}, prev_size = {prev_size}")
            # print(f"index = {index}")
            for j in range( size ):
                u = self.neurons[ index - j] 
                f = u * ( 1 - u )
                d_index = index - self.layer_sizes[0] - j
                
                if i == 0:
                    d[ d_index ] = ( outputs[size-j-1] - u ) * f
                    
                else:
                    d[ d_index ] = 0
                    d_next = d[ 
                        (index-self.layer_sizes[0] + 1) : \
                        (index-self.layer_sizes[0] + next_size + 1) 
                    ]
                    # print(len(d_next))
                    for k in range(next_size):
                        d[ d_index ] += d_next[k] * self.weights[ w_index - k*size ]
                    d[ d_index ] *= f

                # Set weights
                for w in range( prev_size ):
                    self.weights[ w_index - w ] += self.neurons[ index - size - w ] * 0.2 * d[ d_index ]
                w_index -= prev_size
            index -= size
        return d
        
        


    