import arcade
import numpy as np
from brain import *

PLAYER_SCALING = 60/3016
MOVEMENT = 100

INPUTS = 9
OUTPUTS = 3
NEURON_COUNT = 5

class Player(arcade.Sprite):
    def __init__(self, neuron_count, num_inputs, file_name):
        super().__init__("character.png", PLAYER_SCALING)
        weights = np.loadtxt(file_name)
        self.brain = Brain(weights, num_inputs, neuron_count)
        self.center_x = 64
        self.center_y = 250
        self.pos = 0
        self.score = 0

    def draw(self):
        self.draw()

    def update(self, raw):
        player_move = self.brain.get_move(raw)
        self.pos += player_move

        if self.pos >= 4:
            self.pos = 3
        elif self.pos < 0:
            self.pos = 0
        self.center_y = 550-100*self.pos
