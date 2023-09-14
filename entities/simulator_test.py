
import pygame
import time
from widgets import Movable_Object, Obstacle, Button
from commands import parse
from main import main

#intialize game
pygame.init()

#initialize screen
screen = pygame.display.set_mode((1000, 700))
background = pygame.image.load("GUI_Images/Arena.png")
background = pygame.transform.scale(background,(700,700))

TURNING_RAD = 25
SCALE = 3.5

#Title
pygame.display.set_caption("GUI")
"""
set icon below
"""

def game():

    car = Movable_Object([70, 630], "GUI_Images/car with no box.png")
    Movable_Object_Group = pygame.sprite.Group()
    Movable_Object_Group.add(car)

    bounding_box = Movable_Object([70, 630], "GUI_Images/bounding box.png")
    Movable_Object_Group.add(bounding_box)

    sim_button = Button(
        "Simulate",
        (850, 350),
        font=25,
        bg="green"
    )

    res_button = Button(
        "  Reset  ",
        (720, 350),
        font=25,
        bg="red"
    )


    class Simulator():

        def __init__():
            pass

    #Game loop
    clock = pygame.time.Clock()
    running = True
    commands = ["FORWARD 5", "ROTATE 45", "FORWARD 35.35", "ROTATE -45", "REVERSE 5"]

    Obstacle_Group = pygame.sprite.Group()
    #obstacle_list = [[595.0, 595.0, 90], [455.0, 455.0, 0], [472.5, 157.5, 90], [52.5, 367.5, 270], [210.0, 210.0, 180]]
    obstacle_list = [[367.5, 332.5, 90], [542.5,472.5,90], [227.5,472.5, 270],[682.5, 332.5, 180], [455, 140,180]]
    android_string = "ROB:20,20"
    for i in range(len(obstacle_list)):
        x, y , theta = obstacle_list[i]
        x = x//SCALE
        y = (700 - y)//SCALE
        android_string += f";OBS{i+1}:{int(x)},{int(y)},{int(theta)}"

    print(android_string)

    instr = main(android_string)
    print(instr)
    commands = parse(instr)
    print(commands)


    def insert_obstacle(x, y, orientation):
        obstacle = Obstacle([x,y], orientation)
        Obstacle_Group.add(obstacle)


    simulate = False
    reset = False

    while running:

        for x in range(len(obstacle_list)):
            insert_obstacle(obstacle_list[x][0],obstacle_list[x][1], obstacle_list[x][2])
        screen.fill((255,255,255))
        screen.blit(background, (0, 0))

        Movable_Object_Group.update()
        Movable_Object_Group.draw(screen)
        Obstacle_Group.update()
        Obstacle_Group.draw(screen)
        sim_button.show(screen)
        res_button.show(screen)
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

           
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP or event.key == ord('w'):
                    car.move_forward(5, car.angle)
                    bounding_box.move_forward(5, car.angle)

                if event.key == pygame.K_DOWN or event.key == ord('s'):

                    car.move_backward(5, car.angle)
                    bounding_box.move_backward(5, car.angle)

                    
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    car.angle += 45
                    
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    car.angle -= 45

            
            simulate = sim_button.click(event, simulate)
            reset =  res_button.click(event, reset)

        if reset:
            instr = None
            simulate = False
            reset = False
            game()
        
        if simulate:
            if len(commands) == 0:
                instr = None
                simulate = False
            else:
                instr, num = commands.pop(0).split(" ")
                num = float(num)
            
            if instr == "FORWARD":
                car.move_forward(num, car.angle)
                bounding_box.move_forward(num, car.angle)
                pygame.display.update()
                time.sleep(0.2)

            elif instr == "ROTATE":
                car.angle -= int(num)
                pygame.display.update()
                time.sleep(0.2)

            elif instr == "REVERSE":
                car.move_backward(num, car.angle)
                bounding_box.move_backward(num, car.angle)
                pygame.display.update()
                time.sleep(0.2)

            elif instr == "CAPTURE":
                myfont = pygame.font.SysFont('Comic Sans MS', 25)
                textsurface = myfont.render('Capturing Image', False, (0, 0, 0))
                screen.blit(textsurface,(0,0))
                pygame.display.update()
                time.sleep(1)

        
        
          

        pygame.display.update()
        
        if running == False:
            pygame.quit()  
        

if __name__ == "__main__": 
    game()



 