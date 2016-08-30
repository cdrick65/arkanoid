import collections

import pygame

from arkanoid.rounds.base import (BaseRound,
                                  RED)
from arkanoid.sprites.brick import (Brick,
                                    BrickColour)
from arkanoid.sprites.enemy import EnemyType
from arkanoid.sprites.powerup import (CatchPowerUp,
                                      DuplicatePowerUp,
                                      ExtraLifePowerUp,
                                      ExpandPowerUp,
                                      LaserPowerUp)


class Round4(BaseRound):
    """Initialises the background, brick layout and powerups for round 4."""

    _TOP_ROW_START = 5

    def __init__(self, top_offset):
        """Initialise round 4.

        Args:
            top_offset:
                The number of pixels from the top of the screen before the
                top edge can be displayed.
        """
        super().__init__(top_offset)

        self.name = 'Round 4'
        self.enemy_type = EnemyType.cube
        self.num_enemies = 3

    def can_release_enemies(self):
        """Release the enemies right at the start."""
        return True

    def _create_background(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill(RED)
        return background

    def _create_bricks(self):
        """Create the bricks and position them on the screen.

        Returns:
            A pygame.sprite.Group of bricks.
        """
        column = collections.deque(
            [BrickColour.orange, BrickColour.cyan, BrickColour.green,
             BrickColour.silver, BrickColour.blue, BrickColour.pink,
             BrickColour.yellow, BrickColour.white, BrickColour.orange,
             BrickColour.cyan, BrickColour.green, BrickColour.silver,
             BrickColour.blue, BrickColour.pink, BrickColour.white,
             BrickColour.yellow])

        powerups = {  # Keyed by the (x,y) coordinates of the bricks.
            (1, 1): DuplicatePowerUp,
            (2, 3): CatchPowerUp,
            (3, 10): LaserPowerUp,
            (4, 4): ExtraLifePowerUp,
            (7, 11): ExpandPowerUp,
            (8, 0): DuplicatePowerUp,
            (9, 5): LaserPowerUp,
            (10, 7): ExtraLifePowerUp,
        }

        bricks = []

        for x in range(1, 12):
            if x != 6:  # Leave a blank column down the middle.
                for y, colour in enumerate(column):
                    if y < 14:
                        brick = Brick(colour, 4,
                                      powerup_cls=powerups.get((x, y)))
                        bricks.append(
                            self._blit_brick(brick, x,
                                             y + self._TOP_ROW_START))
            column.rotate(-1)

        return pygame.sprite.Group(*bricks)

