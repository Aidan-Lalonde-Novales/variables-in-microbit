# Created By: Aidan L-N
# Created: Sept 28 2020
# 
# Program that increases the counter by 

def on_button_pressed_a():
    global counter
    counter += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(counter)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global counter
    counter += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

# Created By: Aidan L-N
# Created: Sept 28 2020
# 
# Program that sets the counter variable to 0.
counter = 0
counter = 0