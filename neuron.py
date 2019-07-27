import math
import numpy as np

class Neuron():
    def __init__(self, input_weights, output_weights, fitness):
        self.input_weights = input_weights
        self.output_weights = output_weights
        self.fitness = fitness

    def sigmoid(self, x):
        return 1/(math.exp(-x)+1)

    def stimulate(self, inputs):
        hidden = np.dot(self.input_weights, inputs)
        return self.sigmoid(hidden)*self.output_weights

