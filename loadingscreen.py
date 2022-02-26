
#==================
#this file contains the loading screen animation
#==================

from asciimatics.effects import Cycle, Print, BannerText
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def loadingScreen(screen):
    """""
        This function juste call function of the asciimatics
        renderers to display de startting animation.
    """""
    effects = [
            Cycle(
                screen,
                FigletText("REVERSI", font="broadway"),
                int(screen.height / 2 - 8)),
            Print(
                screen,
                FigletText("MADE BY DIEGO", font="Graceful"),
                int(screen.height / 2 +5)
                ),
            BannerText(
                screen,
                FigletText("Press [q] to start", font="Mini"),
                int(screen.height / 2 + 13),
                1
                )]
    screen.play([Scene(effects, 500, True)])
    return

def launch():
    Screen.wrapper(loadingScreen)

