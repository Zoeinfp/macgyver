"""
This is the scene where you can figure out how to play with instructions texts and keyboard arrows image
"""
import pygame as pg
import os
from pygame.locals import *
from config import ASSETS_DIR, SCREEN, COLORS, SCREEN_W, SCREEN_H


class Rules:
    """
    Rules Scene
    """

    def __init__(self):

        # Text fonts
        font = pg.font.Font(None, 42)
        inst_font = pg.font.Font(None, 24)

        # Texts
        text_content = "Mac Gyver Maze"
        inst_content1 = "Use arrows to move around mazes "
        inst_content2 = "collect Swiss knives before facing the enemy."
        inst_content3 = " Wish you will able to 'MacGyver your way out '  !! "
        inst_content4 = "  P = Pause the game / S = Stop the music"

        # Sound
        sound = pg.mixer.Sound(os.path.join(ASSETS_DIR, "sfx/intro.wav"))
        sound.play()

        # Background
        self.background = pg.image.load(os.path.join(ASSETS_DIR, "gfx/splashscreen.png"))

        # Arrows ( image for keys comprehension )
        self.arrows = pg.image.load(os.path.join(ASSETS_DIR, "gfx/arrows.png"))
        self.arrows_rect = self.arrows.get_rect()

        # Title element
        self.title = font.render(text_content, 1, (COLORS["WHITE"]))
        self.title_rect = (font.size(text_content))[0]

        # Instructions element
        self.inst1 = inst_font.render(inst_content1, 1, (COLORS["WHITE"]))
        self.inst2 = inst_font.render(inst_content2, 1, (COLORS["WHITE"]))
        self.inst3 = inst_font.render(inst_content3, 1, (COLORS["WHITE"]))
        self.inst4 = inst_font.render(inst_content4, 1, (COLORS["WHITE"]))

        self.inst_rect1 = (inst_font.size(inst_content1))[0]
        self.inst_rect2 = (inst_font.size(inst_content2))[0]
        self.inst_rect3 = (inst_font.size(inst_content3))[0]
        self.inst_rect4 = (inst_font.size(inst_content4))[0]

        # Launching
        self.run = True
        self.status = 0
        self.draw()

    def update(self):
        """
        Event loop
        """
        while self.run:
            for event in pg.event.get():
                if event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN:
                    self.status = 1
                    self.run = False
                    return self.status

                elif event.type == QUIT:
                    self.status = 0
                    self.run = False
                    return self.status

            pg.time.wait(500)
            self.draw()

    def draw(self):
        """
        Fill background and blit everything to the screen
        """
        # Fill background
        SCREEN.blit(self.background, (0, 0))

        # Blit everything to the screen

        # Text Background
        pg.draw.rect(SCREEN, COLORS["SILVER"], (20, 20, SCREEN_W - 40, SCREEN_H - 40))

        # Text elements ordered by position ( from top to bottom )
        SCREEN.blit(self.title, ((SCREEN_W - self.title_rect) / 2, 60))
        SCREEN.blit(self.inst1, ((SCREEN_W - self.inst_rect1) / 2, 120))
        SCREEN.blit(self.inst2, ((SCREEN_W - self.inst_rect2) / 2, 140))
        SCREEN.blit(self.inst3, ((SCREEN_W - self.inst_rect3) / 2, 340))
        SCREEN.blit(self.inst4, ((SCREEN_W - self.inst_rect4) / 2, 360))

        # Arrows image
        w, h, n = 2, 3, 2.35  # width, height and small adjustment number
        SCREEN.blit(self.arrows, ((SCREEN_W - self.arrows_rect[w] * n), SCREEN_H / 2 - self.arrows_rect[h] / n))

        # Display scene
        pg.display.flip()

        # Slow down process
        pg.time.wait(500)

        # Update Loop
        # ( seeking for new requests )
        self.update()
