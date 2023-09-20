from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_square():
    x, y = 400, 90
    while x < 780:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x += 1
        delay(0.01)
    
    while y < 580:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y += 1
        delay(0.01)

    while x > 20:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x -= 1
        delay(0.01)

    while y > 90:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y -= 1
        delay(0.01)

    while x < 400:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x += 1
        delay(0.01)    

def move_circle():
    center_x, center_y = 400, 335  
    radius = 245 
    angle = -90  

    while angle <= 270:
        clear_canvas()
        grass.draw(400, 30)        
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        character.draw(x, y)
        update_canvas()
        angle += 1
        delay(0.01)
        
while True:
    move_square()
    move_circle()
