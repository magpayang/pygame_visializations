import pygame


class MyRect:
    def __init__(self, screen, screen_width, screen_height, x_pos, y_pos, width, height, color, show=False):
        self.xn = screen
        self.xn_wd = screen_width
        self.xn_ht = screen_height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.wd = width
        self.ht = height
        self.clr = color
        self.show = show

    def __repr__(self):
        return self.ht

    def __str__(self):
        return self.ht

    def __len__(self):
        return self.ht

    def update(self, x_pos, y_pos, width, height, color, show=False):
        if show:
           self.show=True
        else:
            self.show = False

        self.wd = width
        self.ht = height
        self.clr = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        # print(self.y_pos)


    def draw(self):
        if self.show:
            pygame.draw.rect(self.xn, self.clr, [self.x_pos, self.y_pos, self.wd, self.ht])
        else:
            pass

class GroundedRect(MyRect):
    def __init__(self, screen, screen_width, screen_height, x_pos, y_pos, width, height, color, show=False):
        super().__init__(screen, screen_width, screen_height, x_pos, y_pos, width, height, color, show)
        self.x_pos = x_pos
        self.y_pos = self.xn_ht - self.ht - y_pos

    def __repr__(self):
        return self.ht

    def __str__(self):
        return self.ht

    def __len__(self):
        return self.ht


    def update(self, x_pos, y_pos, width, height, color, show=False):
        if show:
           self.show=True
        else:
            self.show = False

        self.wd = width
        self.ht = height
        self.clr = color
        self.x_pos = x_pos
        self.y_pos = self.xn_ht - self.ht - y_pos
