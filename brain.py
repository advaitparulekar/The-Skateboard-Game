import numpy as np
from neuron import *
import math

class Brain():
    def __init__(self, weights, input_size, number):
        self.neurons = []
        self.size = number
        self.neurons = [Neuron(weights[i, 0:input_size], weights[i, input_size:-1], weights[i, -1]) for i in range(number)]

    def get_move(self, raw):
        outputs = np.array([[0.,0.,0.]])
        for neuron in self.neurons:
            outputs+=neuron.stimulate(raw)*neuron.fitness
        return np.argmax(outputs)-1

