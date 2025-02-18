"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
This program executes breakout game. If the user click the
mouse for the 1st time each round, the game starts. If the
ball falls to the ground, lives deducts one. The game will
end if there is no more lives or bricks.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel, GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.graphics.gwindow import GWindow

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    """
    This program executes breakout game.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        graphics.hit_ball_or_brick()

        if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
            graphics.set_dx(-dx)
        if graphics.ball.y < 0:
            graphics.set_dy(-dy)

        # Loses life
        if graphics.ball.y + graphics.ball.height > graphics.window.height:
            graphics.restart()
            lives -= 1
        pause(FRAME_RATE)

        # the game end
        if lives == 0:
            game_over = GLabel('Game Over.')
            game_over.font = '-40'
            graphics.window.add(game_over, graphics.window.width / 2 - game_over.width / 2,
                                graphics.window.height / 2 + game_over.height)
            break
        if graphics.brick_number == 0:
            win = GLabel('You Win!')
            win.font = '-40'
            graphics.window.add(win, (graphics.window.width - win.width) / 2, (graphics.window.height + win.height) / 2)
            graphics.window.remove(graphics.paddle)
            graphics.window.remove(graphics.ball)
            break


if __name__ == '__main__':
    main()
