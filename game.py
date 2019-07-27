import arcade
from column import *
from player import *
from arena import *
import functools

MOVEMENT = 100
GAME_RUNNING = 0
GAME_OVER = 1

NUM_PLAYERS = 100
SURVIVORS = 15
NUM_SAME = 2

NUM_COLS_TRAINED = 2
NEURON_COUNT = 10

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 800, "basicgame")
        arcade.set_background_color(arcade.color.AMAZON)
        self.arena = None
        self.player_list = arcade.SpriteList()
        self.current_state = GAME_RUNNING
        self.first_gen = True
        self.gen_number = 0


    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_list.append(Player(NEURON_COUNT, NUM_COLS_TRAINED*4+5, "../../BasicGameRaw/basic_game/best_player.txt"))
        self.arena = Arena()


    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)


    def draw_game(self):

        self.player_list.draw()
        self.arena.draw()

        output = f"Score: {self.player_list[0].score} \t Generation: {self.gen_number}"
        arcade.draw_text(output, 10, 80, arcade.color.WHITE, 14)
        arcade.draw_line(0, 600, 800, 600, arcade.color.WOOD_BROWN, 10)
        arcade.draw_line(0, 500, 800, 500, arcade.color.WOOD_BROWN, 3)
        arcade.draw_line(0, 400, 800, 400, arcade.color.WOOD_BROWN, 3)
        arcade.draw_line(0, 300, 800, 300, arcade.color.WOOD_BROWN, 3)
        arcade.draw_line(0, 200, 800, 200, arcade.color.WOOD_BROWN, 10)

    def on_draw(self):
        arcade.start_render()

        if self.current_state == GAME_RUNNING:
            self.draw_game()
        else:
            self.setup()
            self.current_state = GAME_RUNNING


    def update(self, delta_time):
        if self.current_state == GAME_RUNNING:            
            for player in self.player_list:
                player_pos_list = [0,0,0,0]
                player_pos_list[player.pos] = 1
                player.update(np.array([1]+self.arena.raw[4:4*NUM_COLS_TRAINED+4]+player_pos_list))
                if self.arena.raw[4+player.pos] == 1:
                    player.score += 1
                if self.arena.raw[4+player.pos] == -1:
                    self.current_state = GAME_OVER
            self.arena.update()


def main():
    game = MyGame()
    game.setup()
    game.set_update_rate(0.3)
    arcade.run()

if __name__ == "__main__":
    main()
