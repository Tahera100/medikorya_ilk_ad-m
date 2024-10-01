from tkinter import * # its important to write like this, cause it used to define the window with Tk().
import random

Game_Width = 700
Game_Height = 700
Speed = 100
Space_Size = 50
Body_Parts = 15
Snake_Color = "#FFFF00"
Food_Color = "#FF69B4"
Background_Color = "black"

class Snake:
    def __init__(self):
        self.body_size = Body_Parts
        self.coordinates = []
        self.snake_bodies = []# to make the rectangle list

        for i in range (0, Body_Parts):
            self.coordinates.append([0,0]) # the starting point is 0,0 in the top left corner

        for x,y in self.coordinates:
            snake_body = canvas.create_rectangle(x,y,x + Space_Size, y + Space_Size,fill= Snake_Color, tag = "snake")
            self.snake_bodies.append(snake_body)
           

    pass

class Food:

    def __init__(self):
        max_columns = Game_Width // Space_Size
        max_rows = Game_Height // Space_Size

        x = random.randint(0, max_columns-1) * Space_Size
        y = random.randint(0, max_rows-1) * Space_Size
        
        self.coordinates = [x,y]

        canvas.create_oval(x,y, x + Space_Size, y + Space_Size, fill= Food_Color, tag = "food")

    pass

def next_action(snake,food):

    x, y = snake.coordinates[0]    # the head of snake 

    if direction == "down":
        y+=Space_Size
    elif direction == "up":
        y-=Space_Size
    
    elif direction == "left":
         x-=Space_Size

    elif direction == "right":
         x+=Space_Size
    
    # to update the coordinate of snake
    snake.coordinates.insert(0,(x,y))
    snake_body = canvas.create_rectangle(x,y, x + Space_Size, y + Space_Size, fill= Snake_Color)    
    snake.snake_bodies.insert(0,snake_body)

    # for eating the food and get big and bigger
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1


        # for increasing the score
        label.config(text="Score:{}".format(score))

        # delete the eaten food and replace with new one in other dimension
        canvas.delete("food")
        food=Food()

    else:
    # delete the last body part of the snake
            del snake.coordinates[-1]
    #update the body part 
            canvas.delete(snake.snake_bodies[-1])
            del snake.snake_bodies[-1]

    if change_collisions(snake):
        game_over()

    else:
    # to call again the next action
         window.after(Speed,next_action,snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def change_collisions(snake):

    x, y = snake.coordinates[0]

# if we are crossing the broders
    if x<0 or x>= Game_Width:
        print("Game is over :( ")
        return True
    elif y<0 or y>= Game_Height:
        print("Game is over :( ")
        return True
    pass
# if it touch it's body parts then game is over
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("Game is over :( ")
            return True

    return False

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2, text=" Game is over :(",font=100 ,fill='red')
    pass


window = Tk()
window.title("Snake Game ")
window.resizable(False, False)  ############################

score = 0
direction = "down"

label = Label(window, text="Score:{}".format(score),font=('newtimes', 30))
label.pack()

#drawing the background with the given height, width and background color.
canvas = Canvas(window, bg=Background_Color, height=Game_Height, width=Game_Width)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# the position of window on the screen fro x and y axies
x = int(800)
y = int(100)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# define the direction of snake through the keys on keyboard
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake= Snake()
food= Food()
next_action(snake,food)

window.mainloop()
