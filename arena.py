import numpy as np
import arcade

COIN_SCALING = 60/200
OBSTACLE_SCALING = 60/250
SPRITE_STARTING = 780
COLUMN_WIDTH = 80
MAX_WIDTH = 10

class Arena():
    def __init__(self):
        self.markov = np.array([[0.15, 0.75, 0.1], [0.1, 0.8, 0.1], [0.1, 0.5, 0.4]])
        self.obstacle_markov = np.array([[0.8, 0.2], [0.6, 0.4], [0.8, 0.2]])
        self.raw = [0,0,0,0]*MAX_WIDTH
        self.coin_list = arcade.SpriteList()
        self.obstacle_list = arcade.SpriteList()
        self.current_clear = 1

    def shift(self):
        self.raw.pop(0)
        self.raw.pop(0)
        self.raw.pop(0)
        self.raw.pop(0)

        for coin in self.coin_list:
            coin.center_x -= COLUMN_WIDTH

        for obstacle in self.obstacle_list:
            obstacle.center_x -= COLUMN_WIDTH

        new_column = [-1, -1, -1, -1]
        new_column[self.current_clear] = 1
        new_column[(self.current_clear+2*np.random.choice(2, p=[0.5, 0.5])-1)%4] = 0
        self.current_clear += np.random.choice(3, p = [0.3, 0.4, 0.3])-1
        if self.current_clear < 0:
            self.current_clear = 0
        if self.current_clear > 3:
            self.current_clear = 3

        """new_column = []
        has_obstacle = False
        for i in range(4):
            if has_obstacle:
                addition = np.random.choice(2, p=self.obstacle_markov[self.raw[-4+i]])
            else:
                addition = np.random.choice(3, p=self.markov[self.raw[-4+i]])-1
                if addition == -1:
                    has_obstacle = True

            new_column.append(addition)
        """

        self.create_sprites(new_column)
        self.raw+=new_column

    def create_sprites(self, column):
        for i in range(4):
            if column[i] == -1:
                new_obstacle = arcade.Sprite("obstacle.png", OBSTACLE_SCALING)
                new_obstacle.center_x = SPRITE_STARTING
                new_obstacle.center_y = 550 - (100*i)
                self.obstacle_list.append(new_obstacle)
            elif column[i] == 1:
                new_coin = arcade.Sprite("coin.png", COIN_SCALING)
                new_coin.center_x = SPRITE_STARTING
                new_coin.center_y = 550 - (100*i)
                self.coin_list.append(new_coin)

    def draw(self):
        self.coin_list.draw()
        self.obstacle_list.draw()

    def update(self):
        self.shift()
        for coin in self.coin_list:
            if coin.center_x < -50:
                coin.kill()
        for obstacle in self.obstacle_list:
            if obstacle.center_x < -50:
                obstacle.kill()
