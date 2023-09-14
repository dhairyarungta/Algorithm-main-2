import pygame
import pygame
from pygame.math import Vector2
import math, time
TURNING_RAD = 25
SCALE = 3.5


obstacle_up = pygame.image.load("GUI_Images/o up.png")
obstacle_down = pygame.image.load("GUI_Images/o down.png")
obstacle_left = pygame.image.load("GUI_Images/o left.png")
obstacle_right = pygame.image.load("GUI_Images/o right.png")

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, orientation):
        super().__init__()
        if orientation == 90:
            self.image = obstacle_up
        elif orientation == 180:
            self.image = obstacle_left
        elif orientation == 270:
            self.image = obstacle_down
        elif orientation == 0:
            self.image = obstacle_right

        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.offset = Vector2(0, 0)
        self.pos = Vector2(pos) 
        self.angle = 0
        self.top_left = (self.pos[0] - 17.5,self.pos[1]-17.5)

    def update(self):
        self.angle = self.angle%360
        self.rotate(self.angle)


    def draw(self, surf):
        surf.blit(self.image, self.pos)


    def rotate(self, angle):
        """Rotate the image of the sprite around a pivot point."""
        # Rotate the image.
        self.image = pygame.transform.rotozoom(self.orig_image, angle, 1)
        # Rotate the offset vector.
        offset_rotated = self.offset.rotate(self.angle)
        # Create a new rect with the center of the sprite + the offset.
        self.rect = self.image.get_rect(center=self.pos+offset_rotated)


class Button:
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, text,  pos, font, bg="black"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.display_text(text, bg)
 
    def display_text(self, text, bg="black"):
        
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()[0] + 20,self.text.get_size()[1] + 20
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (10, 10))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))
 
    def click(self, event, simulate, rst = False, robot = None, bounding_box = None):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if rst:
                        robot.pos[0] = 70
                        robot.pos[1] = 630
                        robot.angle = 0
                        bounding_box.pos[0] = 70
                        bounding_box.pos[1] = 630
                    if not rst:
                        self.display_text("Simulate", bg="grey")
                        return True, time.time()
        
        return False or simulate, None

class Movable_Object(pygame.sprite.Sprite):
    def __init__ (self, pos, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        if picture_path == "GUI_Images/car with no box.png":
            self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0]//3), int(self.image.get_size()[1]//3)))
        self.orig_image = self.image
        print (self.image.get_size())
        self.rect = self.image.get_rect()
        self.offset = Vector2(0, 0)
        self.pos = Vector2(pos) 
        self.angle = 0


    def move_forward(self, distance, angle):
        distance *= SCALE
        # self.pos[0] += distance * (math.sin(angle))
        # self.pos[1] += distance * (math.cos(angle))
        if angle == 0:
            self.pos[1] -= distance
        if angle == 45:
            self.pos[0] -= distance * (1/math.sqrt(2))
            self.pos[1] -= distance * (1/math.sqrt(2))
        if angle == 90:
            self.pos[0] -= distance
        if angle == 135:
            self.pos[0] -= distance * (1/math.sqrt(2))
            self.pos[1] += distance * (1/math.sqrt(2))
        if angle == 180:
            self.pos[1] += distance
        if angle == 225:
            self.pos[0] += distance * (1/math.sqrt(2))
            self.pos[1] += distance * (1/math.sqrt(2))
        if angle == 270:
            self.pos[0] += distance
        if angle == 315:
            self.pos[0] += distance * (1/math.sqrt(2))
            self.pos[1] -= distance * (1/math.sqrt(2))
    
    def move_backward(self, distance, angle):
        distance *= SCALE
        if angle == 0:
            self.pos[1] += distance
        if angle == 45:
            self.pos[0] += distance * (1/math.sqrt(2))
            self.pos[1] += distance * (1/math.sqrt(2))
        if angle == 90:
            self.pos[0] += distance
        if angle == 135:
            self.pos[0] += distance * (1/math.sqrt(2))
            self.pos[1] -= distance * (1/math.sqrt(2))
        if angle == 180:
            self.pos[1] -= distance
        if angle == 225:
            self.pos[0] -= distance * (1/math.sqrt(2))
            self.pos[1] -= distance * (1/math.sqrt(2))
        if angle == 270:
            self.pos[0] -= distance
        if angle == 315:
            self.pos[0] -= distance * (1/math.sqrt(2))
            self.pos[1] += distance * (1/math.sqrt(2))


    def update(self):
        self.angle = self.angle%360
        self.rotate(self.angle)


    def draw(self, surf):
        surf.blit(self.image, self.center)


    def rotate(self, angle):
        """Rotate the image of the sprite around a pivot point."""
        # Rotate the image.
        self.image = pygame.transform.rotozoom(self.orig_image, angle, 1)
        # Rotate the offset vector.
        offset_rotated = self.offset.rotate(self.angle)
        # Create a new rect with the center of the sprite + the offset.
        self.rect = self.image.get_rect(center=self.pos+offset_rotated)
        