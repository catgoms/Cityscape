
#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 10, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
#

# Erect buildings as per the provided city plan

###### Under Construction
def under_construction(x, y, roof_width, roof_height):
    stand_width = 50
    stand_height = 40
    penup()
    goto(x - roof_width/2 + 10, y + roof_height)

    pendown()
    pencolor('black')
    width(4)

    ## Draw the stand
    setheading(90)
    forward(stand_height)
    setheading(0)
    forward(stand_width)
    setheading(270)
    forward(stand_height)
    goto(x - roof_width/2 + 10, y + roof_height + stand_height/2)
    setheading(0)
    forward(stand_width)
    goto(x - roof_width/2 + 10, y + roof_height + stand_height)
    setheading(0)
    forward(stand_width/2)

    ## Draw the connecting part
    width(8)
    setheading(90)
    forward(stand_height//3)

    ## Draw the triangles
    width(2)
    setheading(120)
    for triangle_1 in range(3):
        forward(stand_height*3/4)
        right(120)
    setheading(0)
    for triangle_2 in range(3):
        forward(stand_height/2)
        left(120)
    setheading(0)
    forward(stand_height/2)
    setheading(60)
    forward(stand_height*3/5)
    setheading(180)
    forward(stand_height/2)
    penup()
    goto(x - roof_width/2 + 10 + stand_width/2,
         y + roof_height + stand_height + stand_height//3)

    ## Draw the top parts
    pendown()
    width(4)
    setheading(180)
    forward(stand_width/2 + 10)
    setheading(30)
    forward(stand_height)
    goto(x + roof_width/2 - 20,
         y + roof_height + stand_height + stand_height//3)

    ## Draw the hook
    width(2)
    setheading(270)
    forward(stand_height)
    setheading(225)
    for hook in range(3):
        forward(stand_height/6)
        right(45)

    ## Draw person
    from random import randint
    person_length = 10
    penup()
    goto(x + roof_width/2 - 20,
         y + roof_height + stand_height + stand_height//3 - randint(0, stand_height))
    pendown()
    pencolor('gray')
    width(3)
    
    # Draw person arms
    setheading(315)
    forward(person_length)
    setheading(180)
    forward(person_length*2/3)
    left(180)
    forward(person_length*2/3)
    
    # Draw person head
    setheading(45)
    forward(person_length/2)
    dot(person_length, 'dark salmon')
    penup()
    setheading(120)
    forward(person_length/4)
    dot(person_length//3, 'black')
    right(180)
    forward(person_length//3)
    setheading(225)
    forward(person_length/2)
    pendown()
    
    # Draw person body
    setheading(270)
    forward(person_length*2/3)
    
    # Draw person legs
    setheading(240)
    forward(person_length)
    penup()
    setheading(0)
    forward(person_length)
    pendown()
    setheading(120)
    forward(person_length)
    
    

###### Building A
def building_A(x, y, num_floors, construction_finished):
    
    floors = num_floors - 1 # number of floors excluding ground floor
    max_width = 250 # of the building and the sites
    max_height = 50 # for each floor
    body_width = 80 # of built up floor (not ground floor and roof)
    dent_height = 20 # dented part of ground floor; height and width of cut corners
    dent_width = 50 # dented part of ground floor
        # max_width == body_width * 2 + dent_height * 2 + dent_width
    pencolor('dark red')
    width(1)

    
    ### Draw the floor / building
    penup()
    goto(x-(max_width/2), y)
    fillcolor('misty rose')
    begin_fill()
    pendown()
    setheading(0)
    forward(max_width)
    setheading(90)
    forward(max_height - dent_height)
    goto(x + (max_width/2) - dent_height, y + max_height)
    setheading(90)
    for core_build in range(2): # Draws the body floor
        forward(max_height * floors)
        left(90)
        forward(body_width)
        left(90)
        forward(max_height * floors)
        if core_build == 0: # Draws the dented part
            forward(dent_height)
            setheading(180)
            forward(dent_width)
            setheading(90)
            forward(dent_height)
    goto(x - (max_width/2), y + max_height - dent_height)
    setheading(270)
    forward(max_height - dent_height)
    end_fill()
    penup()

    
    ### Draw a door on ground floor
    door_height = 25
    door_width = 20
    fillcolor('pink')
    goto(x + door_width, y)
    begin_fill()
    pendown()
    setheading(90)
    for doors in range(2): # Draws a rectangle
        forward(door_height)
        left(90)
        forward(door_width * 2)
        left(90)
    end_fill()
    goto(x, y)
    setheading(90)
    forward(door_height)
    penup()


    ### Draw windows on ground floor
    gw_width = 60 # ground window
    gw_height = 30
    fillcolor('powder blue')
    
    # The right window
    goto(x + (dent_width/2) + ((body_width - gw_width)/2),
         y + ((max_height - gw_height)/2)) # bottom left corner of the window
    pendown()
    setheading(0)
    forward(gw_width)
    for ground_right_window in range(1, 4): # Draws the rectangles
        begin_fill()
        pendown()
        setheading(90)
        forward(gw_height/3)
        left(90)
        forward(gw_width)
        left(90)
        forward(gw_height/3)
        penup()
        end_fill()
        goto(x + (dent_width/2) + ((body_width - gw_width)/2) + gw_width,
             y + ((max_height - gw_height)/2) + ((gw_height/3) * ground_right_window))

    # The left window
    goto(x - (dent_width/2) - ((body_width - gw_width)/2),
         y + ((max_height - gw_height)/2)) # bottom right corner of the window
    pendown()
    setheading(180)
    forward(gw_width)
    for ground_left_window in range(1, 4): # Draws the rectangles
        begin_fill()
        pendown()
        setheading(90)
        forward(gw_height/3)
        right(90)
        forward(gw_width)
        right(90)
        forward(gw_height/3)
        penup()
        end_fill()
        goto(x - (dent_width/2) - ((body_width - gw_width)/2) - gw_width,
             y + ((max_height - gw_height)/2) + ((gw_height/3) * ground_left_window))


    ### Draw windows on body floor
    bw_width = 25 # body window
    bw_height = 30
    bw_gap = (body_width-(bw_width*2))/3 # the width of the gap in between the windows
                                         # and the side lines of the building
    fillcolor('lavender')
    if floors > 0: # checks if there is more than one floors
        for body_floors in range(1, num_floors):
            penup()
            goto(x - (dent_width/2) - body_width + bw_gap,
                 y + (max_height - bw_height)/2 + (max_height * body_floors))
                                    # goes to bottom left corner of the window
            for windows in range(4): # draws 4 windows across for each body floor
                begin_fill()
                pendown()
                setheading(0)
                for window in range(2): # draws the rectangle
                    forward(bw_width)
                    left(90)
                    forward(bw_height)
                    left(90)
                penup()
                end_fill()
                if windows == 1: # turtle moves to the right body floor to draw window
                    forward(bw_width + (bw_gap * 2) + dent_width)
                else: # turtle moves right to draw the next window possible
                    forward(bw_width + bw_gap)
                    
            # Draw randomly generated / positioned face and flower
            from random import randint, choice

            # Draw a face
            def face(face_diameter = 16):
                dot(face_diameter, 'dark salmon')
                setheading(180)
                forward(4)
                setheading(90)
                forward(2)
                dot(4, 'black')
                setheading(0)
                forward(8)
                dot(4, 'black')
            # Draw a flower
            def flower():
                flower_diameter = 8
                flower_move = 5
                flower_angle = 45
                setheading(90)
                forward(7)
                for flower in range(4):
                    setheading(flower_angle)
                    forward(flower_move)
                    dot(flower_diameter, 'light coral')
                    setheading(flower_angle - 180)
                    forward(flower_move)
                    flower_angle = flower_angle + 90
                dot(flower_diameter, 'pink')

            face_diameter = 16
            generate = randint(1, 6)
            # draws a face or flower in the first window of the current floor
            if generate == 1:
                goto(x - (dent_width/2) - body_width + bw_gap + bw_width/2,
                     y + (max_height - bw_height)/2 + (max_height * body_floors) +
                         face_diameter/2)
                choice([face, flower])()
                
            generate = randint(1, 6)
            # draws a face or flower in the second window of the current floor
            if generate == 2:
                goto(x - (dent_width/2) - bw_gap - bw_width/2,
                     y + (max_height - bw_height)/2 + (max_height * body_floors) +
                         face_diameter/2)
                choice([face, flower])()
                
            generate = randint(1, 6)
            # draws a face or flower in the third window of the current floor
            if generate == 3: 
                goto(x + (dent_width/2) + bw_gap + bw_width/2,
                     y + (max_height - bw_height)/2 + (max_height * body_floors) +
                         face_diameter/2)
                choice([face, flower])()
                
            generate = randint(1, 6)
            # draws a face or flower in the fourth window of current floor
            if generate == 4: 
                goto(x + (dent_width/2) + body_width - bw_gap - bw_width/2,
                     y + (max_height - bw_height)/2 + (max_height * body_floors) +
                         face_diameter/2)
                choice([face, flower])()


    ### Draw the stairs
    for stairs in range(num_floors):
        if stairs == 2 or stairs == 4 or stairs == 6 or stairs == 8:
                # stairs at every second level / floor
            step_height = (max_height-10)/5 
            step_width = dent_width/5
            goto(x - (dent_width/2), y + step_height + (max_height * stairs))
            fillcolor('burlywood')
            begin_fill()
            pendown()
            for draw_stairs in range(5): # Draws the stairs
                setheading(0)
                forward(step_width)
                setheading(90)
                forward(step_height)
            setheading(270)
            forward(step_height * 2)
            setheading(180)
            forward(step_width/2)
            goto(x - (dent_width/2) + step_width/2, y + (max_height * stairs))
            setheading(180)
            forward(step_width/2)
            setheading(90)
            forward(step_height)
            penup()
            end_fill()

            # Draw handrail for the stairs
            forward(step_height)
            pendown()
            width(2)
            setheading(0)
            goto(x + (dent_width/2) - step_width,
                 y + (max_height * stairs) + max_height - 10 + step_height)
            forward(step_width)
            # Draw handrail bars            
            bar_gap = [3/4, 8/7, 1, 1, 1] 
            for handrail in bar_gap:
                setheading(180)
                forward(step_width*handrail)
                pendown()
                setheading(270)
                forward(step_height)
                penup()
            width(1)

    
    roof_width = max_width - dent_height*2 # the width of only the roof part
    roof_height = max_height * num_floors # top of the building where roof starts

    ### Draw the under construction
    if 'X' in construction_finished:
        under_construction(x, y, roof_width, roof_height)

    ### Draw the roof
    elif 'O' in construction_finished:
        stand_height = 30
        stand_width = body_width/2 # equals to 40
        stand_thickness = 10
        sign_height = 40
        sign_width = dent_width + body_width*2 # equals to 210
        
        letter_width = 50
        letter_thickness = 8

        # Draw the stands on the roof
        fillcolor('indian red')
        pos_neg = [1, -1] # positive for the left roof and negative for the right roof
        stand_status = ['outer', 'inner'] # outer for the stands far from the stairs
                                     # and inner for the stands closer to the stairs
        for stands in pos_neg:
            for status in stand_status:
                if status == 'outer':
                    goto(x + stands*(-max_width/2 + dent_height), y + roof_height)
                else:
                    goto(x + stands*(-dent_width/2), y + roof_height)
                
                begin_fill()
                pendown()
                goto(x + stands*(-dent_width/2 - body_width/2),
                     y + roof_height + stand_height)
                setheading(270)
                forward(stand_thickness)

                if status == 'outer':
                    goto(x + stands*(-max_width/2 + dent_height + stand_thickness),
                         y + roof_height)
                else:
                    goto(x + stands*(-dent_width/2 - stand_thickness), y + roof_height)

                penup()
                end_fill()

        # Draw the sign on the roof
        fillcolor('papaya whip')
        width(2)
        start_point = x - max_width/2 + dent_height + (sign_width - letter_width*4)/2
            # left side of the sign
        goto(start_point, y + roof_height + max_height) # top left corner of the sign
        begin_fill()
        pendown()

        # Draw top of T
        setheading(0)
        forward(letter_width)

        # Draw top of W
        forward(letter_thickness/2)
        goto(start_point + letter_width + letter_thickness*3/2,
             y + roof_height + max_height - sign_height + letter_thickness)
        goto(start_point + letter_width + (letter_width - letter_thickness)/2,
             y + roof_height + max_height - sign_height/4)
        setheading(0)
        forward(letter_thickness)
        goto(start_point + letter_width*2 - letter_thickness*3/2,
             y + roof_height + max_height - sign_height + letter_thickness)
        goto(start_point + letter_width*2 - letter_thickness/2,
             y + roof_height + max_height)
        setheading(0)
        forward(letter_thickness/2)

        # Draw top of I
        setheading(0)
        forward(letter_width)

        # Draw N
        forward(letter_thickness)
        goto(start_point + letter_width*4 - letter_thickness,
             y + roof_height + max_height - sign_height + letter_thickness)
        setheading(90)
        forward(sign_height - letter_thickness)
        setheading(0)
        forward(letter_thickness)
        setheading(270)
        forward(sign_height)
        setheading(180)
        forward(letter_thickness)
        goto(start_point + letter_width*3 + letter_thickness,
             y + roof_height + max_height - letter_thickness)

        # Draw part of I
        setheading(180)
        for i_lines in range(2):
            penup()
            forward(letter_thickness)
            pendown()
            forward((letter_width - letter_thickness)/2)

        # Draw W
        goto(start_point + letter_width*2 - letter_thickness,
             y + roof_height + max_height - sign_height)
        setheading(180)
        forward(letter_thickness)
        goto(start_point + letter_width*3/2,
             y + roof_height + max_height - sign_height/4 - letter_thickness)
        goto(start_point + letter_width + letter_thickness*2,
             y + roof_height + max_height - sign_height)
        setheading(180)
        forward(letter_thickness)
        goto(start_point + letter_width,
             y + roof_height + max_height - letter_thickness)

        # Draw T
        setheading(180)
        forward((letter_width - letter_thickness)/2)
        setheading(270)
        forward(sign_height - letter_thickness)
        setheading(180)
        forward(letter_thickness)
        setheading(90)
        forward(sign_height - letter_thickness)
        setheading(180)
        forward((letter_width - letter_thickness)/2)
        setheading(90)
        forward(letter_thickness)
        
        end_fill()

        # Draw rest part of I
        penup()
        goto(start_point + letter_width*2 + (letter_width - letter_thickness)/2,
             y + roof_height + max_height - letter_thickness)
        begin_fill()
        pendown()    
        setheading(270)
        forward(sign_height - letter_thickness*2)
        setheading(180)
        forward((letter_width - letter_thickness)/2)
        setheading(270)
        forward(letter_thickness)
        setheading(0)
        forward(letter_width + letter_thickness)
        setheading(90)
        forward(sign_height - letter_thickness)
        penup()
        setheading(180)
        forward(letter_thickness)
        pendown()
        setheading(270)
        forward(sign_height - letter_thickness*2)
        setheading(180)
        forward((letter_width - letter_thickness)/2)
        setheading(90)
        forward(sign_height - letter_thickness*2)
        end_fill()



###### Building B
def building_B(x, y, num_floors, construction_finished):

    max_width = 240 # ground concrete
    gutter_height = 6
    ground_width = 220 # ground floor
    ground_height = 64 # ground floor
    body_height = 44 # body (built up) floors
    body_width = 200 # body (built up) floors

    main_door_width = 50 # ground floor door
    main_door_height = 50 # ground floor door
    door_width = 20 # body floor door
    door_height = 30 # body floor door
    door_edge_width = 5
    difference = 10

    pencolor('darkblue')
    width(1)


    ### Draw the ground floor
    penup()

    # Draw the concrete
    goto(x - max_width/2, y)
    fillcolor('silver')
    begin_fill()
    pendown()
    setheading(0)
    for concrete in range(2):
        forward(max_width)
        left(90)
        forward(gutter_height)
        left(90)
    end_fill()
    penup()

    for concrete_stairs in [-1, +1]:
        goto(x + concrete_stairs*(main_door_width/2 + difference), y)
        pendown()
        setheading(90)
        forward(gutter_height)
        penup()
    goto(x - main_door_width/2 - difference, y + gutter_height/2)
    pendown()
    setheading(0)
    forward(main_door_width + difference*2)
    penup()

    # Draw the building
    fillcolor('paleturquoise') # Color in blue
    goto(x - ground_width/2, y + gutter_height)
    begin_fill()
    setheading(90)
    forward(ground_height)
    right(90)
    forward(ground_width)
    right(90)
    forward(ground_height)
    end_fill()

    fillcolor('crimson') # Color red stripe
    setheading(90)
    forward(difference)
    begin_fill()
    setheading(180)
    forward(ground_width)
    right(90)
    forward(difference)
    right(90)
    forward(ground_width)
    end_fill()

    goto(x - ground_width/2, y + gutter_height) # Draw the outlines
    pendown()
    setheading(90)
    forward(ground_height)
    right(90)
    forward(ground_width)
    right(90)
    forward(ground_height)
    penup()

    # Draw the top
    goto(x - max_width/2, y + gutter_height + ground_height)
    fillcolor('chocolate')
    begin_fill()
    pendown()
    setheading(0)
    forward(max_width)
    goto(x + body_width/2, y + gutter_height*2 + ground_height)
    setheading(180)
    forward(body_width)
    goto(x - max_width/2, y + gutter_height + ground_height)
    end_fill()
    penup()

    # Draw the door edge
    goto(x - main_door_width/2 - difference/2, y + gutter_height)
    fillcolor('chocolate')
    begin_fill()
    pendown()
    setheading(90)
    forward(main_door_width - difference)
    goto(x - main_door_width/2 + difference,
         y + gutter_height + main_door_height + difference/2)
    setheading(0)
    forward(main_door_width - difference*2)
    goto(x + main_door_width/2 + difference/2,
         y + gutter_height + main_door_height - difference)
    setheading(270)
    forward(main_door_width - difference)
    end_fill()
    penup()

    # Draw the main door
    goto(x + main_door_width/2, y + gutter_height)
    fillcolor('sienna')
    begin_fill()
    pendown()
    setheading(90)
    forward(main_door_height/2)
    circle(main_door_height/2, 180)
    forward(main_door_height/2)
    end_fill()
    goto(x, y + gutter_height)
    setheading(90)
    forward(main_door_height)
    penup()
    goto(x + difference/2, y + gutter_height + main_door_height/3)
    dot(difference/2, 'gold')
    goto(x - difference/2, y + gutter_height + main_door_height/3)
    dot (difference/2, 'gold')


    ### Draw the body floor
    for floors in range(num_floors):
        floor = floors - 1
        floors_height = ground_height + gutter_height*(2+floor) + body_height*floors
        floor_height = ground_height + gutter_height*(2+floor) + body_height*floor
        if floors > 0:
            if floors > 1:
                body_width = body_width - difference
            goto(x - body_width/2,
                 y + floor_height)
            # Draw the building
            fillcolor('paleturquoise')
            begin_fill()
            pendown()
            setheading(90)
            forward(body_height)
            setheading(0)
            forward(body_width)
            setheading(270)
            forward(body_height)
            end_fill()
            penup()

            # Draw the door
            goto(x + door_width/2, y + floor_height)
            fillcolor('dimgray')
            begin_fill()
            pendown()
            setheading(90)
            forward(door_height*2/3)
            circle(door_width/2, 180)
            forward(door_height*2/3)
            end_fill()
            penup()
            
            # Draw the door curtains
            goto(x - door_width/2, y + floor_height + door_height/3)
            fillcolor('firebrick')
            begin_fill()
            pendown()
            
            goto(x - door_width/2 + door_width//6,
                 y + floor_height + door_height/3 + door_width//6)
            
            goto(x - door_width/2 + door_width//3,
                 y + floor_height + door_height/3 + door_width//3)
            
            goto(x, y + floor_height + door_height*5/6)
            
            goto(x + door_width/2 - door_width//3,
                 y + floor_height + door_height/3 + door_width//3)
            
            goto(x + door_width/2 - door_width//6,
                 y + floor_height + door_height/3 + door_width//6)
            
            goto(x + door_width/2,
                 y + floor_height + door_height/3)
            
            setheading(90)
            forward(door_height/3)
            circle(door_width/2, 180)
            forward(door_height/3)
            end_fill()
            penup()

            # Draw the windows
            for windows in [-1, +1]:
                goto(x + windows*(door_width/2 + (body_width-door_width)/4),
                     y + floor_height + body_height/2)
                shape('square')
                color('cadetblue')
                shapesize(1, 1)
                setheading(45)
                stamp()
            shape('classic')
            color('darkblue')
            
            # Draw the left decoration
            if floors==1 or floors==3 or floors==5 or floors==7 or floors==9:
                goto(x - body_width/2 - difference, y + floors_height)
                pendown()
                setheading(240)
                forward(difference)
                dot(difference, 'red')
                setheading(290)
                forward(difference)
                fillcolor('white')
                begin_fill()
                setheading(20)
                forward(gutter_height/2)
                for decoration in range(2):
                    right(90)
                    forward(gutter_height*2)
                    right(90)
                    forward(gutter_height)
                end_fill()
                penup()
                
            # Draw the right decoration
            if floors==2 or floors==4 or floors==6 or floors==8:
                goto(x + body_width/2 + difference, y + floors_height)
                pendown()
                setheading(300)
                forward(difference)
                dot(difference, 'red')
                setheading(250)
                forward(difference)
                fillcolor('white')
                begin_fill()
                setheading(340)
                forward(gutter_height/2)
                for decoration in range(2):
                    right(90)
                    forward(gutter_height*2)
                    right(90)
                    forward(gutter_height)
                end_fill()
                penup()

            # Draw the top
            goto(x - body_width/2 - difference, y + floors_height)
            fillcolor('chocolate')
            begin_fill()
            pendown()
            setheading(0)
            forward(body_width + difference*2)
            goto(x + body_width/2 - difference/2,
                 y + floors_height + gutter_height)
            setheading(180)
            forward(body_width - difference)
            goto(x - body_width/2 - difference, y + floors_height)
            end_fill()
            penup()


    roof_width = body_width
    roof_height = floors_height + gutter_height

    ### Draw the under construction
    if 'X' in construction_finished:
        under_construction(x, y, roof_width, roof_height)

    ### Draw the roof
    elif 'O' in construction_finished:
        # Draw the bottom part
        if num_floors == 10 or num_floors == 9:
            # building with 9 or 10 floors has fixed width
            goto(x - difference*2, y + floors_height + gutter_height)
        else:
            # buildings with lesser floors are wider
            goto(x - difference*11 + difference*num_floors,
                 y + floors_height + gutter_height)
        fillcolor('paleturquoise')
        begin_fill()
        pendown()
        goto(x - difference,
             y + floors_height + gutter_height + body_width/12)
        penup()
        setheading(0)
        forward(difference*2)
        pendown()
        if num_floors == 10 or num_floors == 9:
            # building with 9 or 10 floors has fixed width
            goto(x + difference*2, y + floors_height + gutter_height)
        else:
            # others gets wider as it has lesser floors
            goto(x + difference*11 - difference*num_floors,
                 y + floors_height + gutter_height)
        end_fill()
        goto(x + difference,
             y + floors_height + gutter_height + body_width/12)
        
        # Draw the middle part
        fillcolor('cornflowerblue')
        begin_fill()
        setheading(90)
        for mid in range(2):
            forward(difference/2)
            left(90)
            forward(difference*2)
            left(90)
        forward(difference/2)
        end_fill()
        
        # Draw the round part
        fillcolor('paleturquoise')
        begin_fill()
        setheading(0)
        for half_circle in range(2):
            circle(difference/2, 180)
            forward(difference*2)
        end_fill()
        penup()
        setheading(90)
        forward(difference)
        
        # Draw the indented part
        fillcolor('cornflowerblue')
        begin_fill()
        pendown()
        setheading(150)
        forward(difference/2)
        setheading(30)
        forward(difference/2)
        goto(x - difference,
             y + floors_height + gutter_height + body_width/12 + difference*2)
        setheading(330)
        forward(difference/2)
        setheading(210)
        forward(difference/2)
        end_fill()
        penup()
        goto(x + difference,
             y + floors_height + gutter_height + body_width/12 + difference*2)
        
        # Draw the triangle part
        fillcolor('paleturquoise')
        begin_fill()
        pendown()
        goto(x, y + floors_height + gutter_height + body_width/12  + difference*4)
        goto(x - difference,
             y + floors_height + gutter_height + body_width/12 + difference*2)
        end_fill()
        penup()
        goto(x, y + floors_height + gutter_height + body_width/12  + difference*4)
        dot(difference/2, 'gold')

        

###### Building C
def building_C(x, y, num_floors, construction_finished):

    max_width = 200
    body_width = 120
    body_height = 40

    pencolor('black')
    width(1)


    ### Draw the ground floor
    back_height = 20 # Variations for placing rocks
    size = 10 # Variations for placing rocks
    
    # Draw the rock
    def rocks(x, y, rock_size = 10):
        fillcolor('gray')
        goto(x, y)
        begin_fill()
        pendown()
        setheading(90)
        forward(rock_size)
        setheading(50)
        forward(rock_size)
        setheading(0)
        forward(rock_size*3/2)
        setheading(330)
        forward(rock_size)
        setheading(270)
        forward(rock_size)
        setheading(240)
        forward(rock_size)
        setheading(180)
        forward(rock_size*3/2)
        goto(x, y)
        end_fill()
        penup()
        setheading(45)
        forward(rock_size)
        shape('square')
        color('white')
        shapesize(0.3, 0.3)
        stamp()
        color('black')
        shape('classic')
    
    # Draw the back rocks on the ground
    penup()
    rocks(x - max_width/2, y + back_height)
    rocks(x - max_width/2 + size*3, y + back_height + size/2, 15)
    rocks(x + max_width/2 - size*6, y + back_height + size)
    rocks(x + max_width/2 - size*4, y + back_height + size/2, 14)


    ### Draw the building
    goto(x - body_width/2, y + (back_height+size)/2)
    fillcolor('peru')
    begin_fill()
    pendown()
    setheading(90)
    for ground in range(2): # Draws the building
        forward(body_height * num_floors)
        right(90)
        forward(body_width)
        right(90)
    end_fill()
    penup()
    
    for hor_bricks in range(num_floors*2): # Draws the horizontal lines
        goto(x - body_width/2,
             y + (back_height+size)/2 + (body_height/2)*hor_bricks)
        pendown()
        setheading(0)
        forward(body_width)
        penup()
        setheading(90)
        
    for ver_bricks_1 in range(num_floors): # Draws the lines on every second row
        goto(x - body_width/2 + body_width/3,
             y + ((back_height+size)/2) + body_height*ver_bricks_1)
        fillcolor('brown')
        begin_fill()
        pendown()
        forward(body_height/2)
        penup()
        goto(x + body_width/2 - body_width/3,
             y + ((back_height+size)/2) + body_height*ver_bricks_1)
        pendown()
        forward(body_height/2)
        end_fill()
        penup()
        forward(body_height/2)
        
    for ver_bricks_2 in range(num_floors): # Draws the vertical lines in the middle
        goto(x, y + ((back_height+size)/2) + body_height*ver_bricks_2)
        penup()
        forward(body_height/2)
        pendown()
        forward(body_height/2)
        
    for ver_bricks_3 in range(num_floors): # Draws the vertical lines on the left
        penup()
        goto(x - body_width/2 + body_width/6,
             y + ((back_height+size)/2) + body_height*ver_bricks_3)
        forward(body_height/2)
        pendown()
        forward(body_height/2)
        
    for ver_bricks_4 in range(num_floors): # Draws the 5th vertical lines
        penup()
        goto(x + body_width/2 - body_width/6,
             y + ((back_height+size)/2) + body_height*ver_bricks_4)
        forward(body_height/2)
        pendown()
        forward(body_height/2)

    # Draw the flower windows
    for flower in range(2, num_floors+1):
        penup()
        if flower==2 or flower==5 or flower==8:
            goto(x - body_width/2 + body_width/6,
                 y + (back_height+size)/2 + body_height*flower - body_height/2)
        elif flower==3 or flower==6 or flower==9:
            goto(x,
                 y + (back_height+size)/2 + body_height*flower - body_height/2)
        elif flower==4 or flower==7 or flower==10:
            goto(x + body_width/2 - body_width/6,
                 y + (back_height+size)/2 + body_height*flower - body_height/2)
        setheading(90)
        forward(body_height/5)
        setheading(135)
        fillcolor('rosybrown')
        begin_fill()
        pendown()
        for flower_petal in range(4):
            circle(body_height/5, 180)
            right(90)
        end_fill()

    # Draw the front rocks on the ground floor
    penup()
    rocks(x - max_width/2 + size*2, y + back_height/2, 13)
    rocks(x - max_width/2 + size*5, y + back_height, 16)
    rocks(x + max_width/2 - size*3, y + back_height/2 + size, 11)
    rocks(x + size*3, y + back_height/2, 15)

    # Draw the flowers on the ground floor
    def ground_flower(petal_color, stigma_color):        
        flower_diameter = 10
        flower_move = 7
        flower_angle = 45
        setheading(90)
        forward(flower_move)
        for flower in range(4): # Draw the petals
            setheading(flower_angle)
            forward(flower_move)
            dot(flower_diameter, petal_color)
            setheading(flower_angle - 180)
            forward(flower_move)
            flower_angle = flower_angle + 90
        dot(flower_diameter, stigma_color) # Draw the stigma

    # Draw the flower and stem
    width(2)
    color('darkgreen')
    goto(x, y)
    pendown()
    setheading(100)
    forward(back_height/2)
    setheading(120)
    forward(back_height/2)
    penup()
    ground_flower('indigo', 'violet')

    goto(x + size*2, y + size/2)
    pendown()
    setheading(70)
    forward(back_height/2)
    setheading(50)
    forward(back_height/2)
    penup()
    ground_flower('royalblue', 'gold')


    roof_width = body_width
    roof_height = (back_height+size)/2 + body_height * num_floors

    ### Draw the under construction
    if 'X' in construction_finished:
        under_construction(x, y, roof_width, roof_height)

    ### Draw the roof
    elif 'O' in construction_finished:
        roof_start = body_height * num_floors + (back_height+size)/2
            # The height where roof starts
        roof_width = body_width + 60 # equals 180
        roof_bottom = 30 # Roof bottom part height
        roof_body = 70 # Roof body part height
        roof_top = 10 # Roof top part height
        stand_width = 20

        color('black')
        width(1)


        ## Draw the roof bottom
        penup()
        goto(x - body_width/2, y + roof_start)
        fillcolor('dimgrey')
        begin_fill()
        pendown()
        goto(x - roof_width/2, y + roof_start + roof_bottom)
        setheading(0)
        forward(roof_width)
        goto(x + body_width/2, y + roof_start)
        end_fill()
        penup()

        # Draw the stands
        
        # First stand
        goto(x - body_width/2 + stand_width/2, y + roof_start)
        fillcolor('sienna')
        begin_fill()
        pendown()
        goto(x - roof_width/2 + stand_width, y + roof_start + roof_bottom)
        setheading(0)
        forward(stand_width*1.5)
        goto(x - body_width/2 + stand_width*1.5, y + roof_start)
        end_fill()
        penup()
        
        # Second stand
        goto(x - stand_width/2, y + roof_start)
        begin_fill()
        pendown()
        goto(x - stand_width*2/3, y + roof_start + roof_bottom)
        setheading(0)
        forward(stand_width*4/3)
        goto(x + stand_width/2, y + roof_start)
        end_fill()
        penup()
        
        # Third stand
        goto(x + body_width/2 - stand_width/2, y + roof_start)
        begin_fill()
        pendown()
        goto(x + roof_width/2 - stand_width, y + roof_start + roof_bottom)
        setheading(180)
        forward(stand_width*1.5)
        goto(x + body_width/2 - stand_width*1.5, y + roof_start)
        end_fill()
        penup()


        ## Draw the body part
        goto(x - roof_width/2, y + roof_start + roof_bottom)
        fillcolor('blanched almond')
        begin_fill()
        pendown()
        setheading(90)
        forward(roof_body)
        setheading(0)
        forward(roof_width)
        setheading(270)
        forward(roof_body)
        end_fill()
        pendown()

        # Draw the fence decoration
        pencolor('saddlebrown')
        width(3)
        goto(x - roof_width/2, y + roof_start + roof_bottom)
        pendown()
        setheading(90)
        forward(roof_width/6)
        width(5)
        setheading(0)
        forward(roof_width)
        width(3)
        setheading(270)
        forward(roof_width/6)
        setheading(180)
        forward(roof_width)
        for cross1 in range(6):
            goto(x - roof_width/2 + roof_width/6*(cross1+1),
                 y + roof_start + roof_bottom + roof_width/6)
            goto(x - roof_width/2 + roof_width/6*(cross1+1),
                 y + roof_start + roof_bottom)
        for cross2 in range(6):
            goto(x + roof_width/2 - roof_width/6*(cross2+1),
                 y + roof_start + roof_bottom + roof_width/6)
            goto(x + roof_width/2 - roof_width/6*(cross2+1),
                 y + roof_start + roof_bottom)
        penup()
        pencolor('black')
        width(1)


        ## Draw the top part
        goto(x - roof_width/2,
             y + roof_start + roof_bottom + roof_body)
        fillcolor('Tan')
        begin_fill()
        pendown()
        setheading(90)
        forward(roof_top*3/2)
        setheading(0)
        forward(roof_top/2)
        for top_part in range(8):
            setheading(270)
            forward(roof_top)
            setheading(0)
            forward(roof_top)
            setheading(90)
            forward(roof_top)
            setheading(0)
            forward(roof_top)
        setheading(270)
        forward(roof_top)
        setheading(0)
        forward(roof_top)
        setheading(90)
        forward(roof_top)
        setheading(0)
        forward(roof_top/2)
        setheading(270)
        forward(roof_top*3/2)
        end_fill()
        penup()
        

        ## Draw the room
        room_width = 50
        room_bottom = 10
        room_body = 50
        room_top = 8
        room_point = (roof_body-room_bottom-room_body)/2 + roof_start + roof_bottom
            # y-cor for the bottom point of the room
        gap = 10

        # Draw the room bottom
        goto(x + roof_width/2 - room_width/2 - gap,
             y + room_point)
        fillcolor('steelblue')
        begin_fill()
        pendown()
        goto(x + roof_width/2 - room_width - gap,
             y + room_point + room_bottom)
        setheading(0)
        forward(room_width)
        goto(x + roof_width/2 - room_width/2 - gap,
             y + room_point)
        end_fill()
        goto(x + roof_width/2 - room_width/2 - gap - room_width//6,
             y + room_point + room_bottom)
        setheading(0)
        forward(room_width//6 * 2)
        goto(x + roof_width/2 - room_width/2 - gap,
             y + room_point)
        penup()

        # Draw the room body
        goto(x + roof_width/2 - room_width - gap,
             y + room_point + room_bottom)
        fillcolor('blanched almond')
        begin_fill()
        pendown()
        setheading(90)
        for room in range(2):
            forward(room_body)
            right(90)
            forward(room_width)
            right(90)
        end_fill()
        penup()

        # Draw the bricks
        fillcolor('peru')
        begin_fill()
        pendown()
        setheading(90)
        for brick_bottom in range(2):
            forward(room_body/5)
            right(90)
            forward(room_width)
            right(90)
        end_fill()
        setheading(90)
        forward(room_body)
        begin_fill()
        for brick_top in range(2):
            right(90)
            forward(room_width)
            right(90)
            forward(room_body/5)
        end_fill()
        penup()
        
        goto(x + roof_width/2 - room_width/2 - gap,
             y + room_point + room_bottom)
        pendown()
        setheading(90)
        forward(room_body/5)
        setheading(0)
        forward(room_width/4)
        setheading(270)
        forward(room_body/5)
        setheading(180)
        forward(room_width/2)
        setheading(90)
        forward(room_body/5)
        penup()

        goto(x + roof_width/2 - room_width/2 - gap,
             y + room_point + room_bottom + room_body*4/5)
        pendown()
        setheading(90)
        forward(room_body/5)
        setheading(0)
        forward(room_width/4)
        setheading(270)
        forward(room_body/5)
        setheading(180)
        forward(room_width/2)
        setheading(90)
        forward(room_body/5)
        penup()
        
        # Draw veranda
        goto(x + roof_width/2 - gap - room_width/5,
             y + room_point + room_bottom + room_body/5)
        fillcolor('grey')
        begin_fill()
        pendown()
        setheading(90)
        forward(room_body*3/5)
        setheading(180)
        forward(room_width*3/5)
        setheading(270)
        forward(room_body*3/5)
        end_fill()
        penup()

        # Draw the hair
        plait = 10
        plait_width = 14
        goto(x + roof_width/2 - 12 - room_width/5,
             y + room_point + room_bottom + room_body/5)
        fillcolor('gold')
        begin_fill()
        pendown()
        # Main Part
        setheading(270)
        forward(plait*4)
        setheading(225)
        forward(plait)
        setheading(135)
        forward(plait)
        setheading(90)
        forward(plait*4)
        # Rounded top part
        setheading(180)
        forward(plait/2)
        setheading(20)
        forward(plait)
        setheading(0)
        forward(plait/2)
        goto(x + roof_width/2 - (gap+2) - room_width/5,
             y + room_point + room_bottom + room_body/5)
        end_fill()
        penup()
        # Tie
        setheading(270)
        forward(plait*4)
        setheading(225)
        forward(plait/2)
        fillcolor('red')
        begin_fill()
        pendown()
        setheading(180)
        for tie in range(2):
            forward(plait_width/2)
            left(90)
            forward(plait/2)
            left(90)
        end_fill()
        penup()
        setheading(270)
        forward(plait/2)
        # End Part
        fillcolor('gold')
        begin_fill()
        pendown()
        setheading(290)
        forward(plait)
        setheading(270)
        forward(plait)
        setheading(250)
        forward(plait)
        setheading(210)
        forward(plait)
        setheading(60)
        forward(plait/2)
        setheading(80)
        forward(plait/2)
        setheading(110)
        forward(plait)
        setheading(90)
        forward(plait)
        goto(x + roof_width/2 - (gap+2) - room_width/5 - plait_width*3/4,
             y + room_point + room_bottom + room_body/5 - plait*4.75)
        setheading(0)
        forward(plait_width/2)
        end_fill()
        penup()
        # Detail
        color('orangered')
        width(1)
        goto(x + roof_width/2 - gap - room_width/5 - plait,
             y + room_point + room_bottom*3/2)
        pendown()
        setheading(270)
        forward(plait*3/2)
        penup()
        forward(plait*2)
        setheading(315)
        forward(plait//3)
        pendown()
        setheading(70)
        forward(plait/2)
        setheading(90)
        forward(plait)
        penup()
        setheading(270)
        forward(plait*2.5)
        setheading(180)
        forward(plait/4)
        pendown()
        setheading(280)
        forward(plait/2)
        setheading(270)
        forward(plait)
        penup()
        
        

###### Building D
def building_D(x, y, num_floors, construction_finished):

    max_width = 220
    max_height = 60

    door_floor = 40
    door_width = 20
    door_height = 30
    bridge_width = max_width - door_floor*2 # equals to 140
    bridge_height = 20

    pencolor('saddlebrown')
    width(1)

    ### Draw the ground floor

    # Draw the stairs
    stair_width = 120
    stair_height = 5
    for stairs in range(12):
        goto(x - stair_width/2 + stair_height*stairs, y + stair_height*stairs)
        fillcolor('sandybrown')
        begin_fill()
        pendown()
        setheading(0)
        for drawing_stairs in range(2):
            forward(stair_width - stair_height*2*stairs)
            left(90)
            forward(stair_height)
            left(90)
        end_fill()
        penup()

    
    penup()
    goto(x - max_width/2, y)
    fillcolor('peachpuff')
    begin_fill()
    pendown()
    setheading(0)
    forward(door_floor)

    # Draw the bottom bridge
    goto(x - max_width/2 + door_floor + bridge_width/7, y + bridge_height/2)
    goto(x - max_width/2 + door_floor + bridge_width*2/5, y + bridge_height)
    setheading(0)
    forward(bridge_width/5)
    goto(x + max_width/2 - door_floor - bridge_width/7, y + bridge_height/2)
    goto(x + max_width/2 - door_floor, y)

    # Continue drawing the ground floor
    setheading(0)
    forward(door_floor)
    setheading(90)
    forward(max_height)
    setheading(180)
    forward(door_floor)
    setheading(270)
    forward(bridge_height)
    setheading(180)
    forward(bridge_width)
    setheading(90)
    forward(bridge_height)
    setheading(180)
    forward(door_floor)
    setheading(270)
    forward(max_height)
    end_fill()
    penup()
    
    # Draw the stripes
    stripe = 10
    goto(x - max_width/2 + (door_floor - stripe)/2, y)
    fillcolor('saddlebrown')
    begin_fill()
    pendown()
    setheading(90)
    forward(max_height)
    setheading(0)
    forward(stripe)
    setheading(270)
    forward(max_height)
    end_fill()
    penup()

    goto(x + max_width/2 - (door_floor - stripe)/2, y)
    begin_fill()
    pendown()
    setheading(90)
    forward(max_height)
    setheading(180)
    forward(stripe)
    setheading(270)
    forward(max_height)
    end_fill()
    penup()

    # Draw the doors
    # Left door
    goto(x - max_width/2 + (door_floor-door_width)/2, y)
    fillcolor('lemonchiffon')
    begin_fill()
    pendown()
    setheading(90)
    forward(door_height)
    right(90)
    forward(door_width)
    right(90)
    forward(door_height)
    end_fill()
    penup()
    # Right door
    goto(x + max_width/2 - (door_floor-door_width)/2, y)
    begin_fill()
    pendown()
    setheading(90)
    forward(door_height)
    left(90)
    forward(door_width)
    left(90)
    forward(door_height)
    end_fill()
    penup()

    # Write text
    goto(x, y + bridge_height*4/5)
    write("WELCOME", align="center", font=("Broadway", 16, "normal"))


    for floors in range(num_floors):
        if floors != 0:
            ### Draw the graden part
            
            ## Draw the bottom concrete
            concrete = 5 # concrete height
            goto(x - max_width/2, y + max_height*floors)
            fillcolor('gray')
            begin_fill()
            pendown()
            setheading(0)
            for draw_concrete in range(2):
                forward(max_width)
                left(90)
                forward(concrete)
                left(90)
            end_fill()
            penup()


            ## Draw the pillars
            pillar_width = 25
            short = 2.5
            long_height = max_height - concrete*2 - short*4

            # Left pillar
            goto(x - max_width/2, y + max_height*floors + concrete)
            fillcolor('cornsilk')
            begin_fill()
            pendown()
            setheading(90)
            for stand_bottom in range(2):
                forward(short)
                right(90)
                forward(short)
                left(90)
            setheading(90)
            forward(long_height)
            setheading(180)
            for stand_top in range(2):
                forward(short)
                right(90)
                forward(short)
                left(90)
            setheading(0)
            forward(pillar_width)
            setheading(270)
            for stand_top in range(2):
                forward(short)
                right(90)
                forward(short)
                left(90)
            setheading(270)
            forward(long_height)
            setheading(0)
            for stand_bottom in range(2):
                forward(short)
                right(90)
                forward(short)
                left(90)
            end_fill()
            penup()

            for pillar_detail in range(2):
                goto(x - max_width/2 + short*(4 + pillar_detail*2),
                     y + max_height*floors + concrete + short*2)
                pendown()
                setheading(90)
                forward(long_height)
                penup()

            # Right pillar
            goto(x + max_width/2, y + max_height*floors + concrete)
            fillcolor('cornsilk')
            begin_fill()
            pendown()
            setheading(90)
            for stand_bottom in range(2):
                forward(short)
                left(90)
                forward(short)
                right(90)
            setheading(90)
            forward(long_height)
            setheading(0)
            for stand_top in range(2):
                forward(short)
                left(90)
                forward(short)
                right(90)
            setheading(180)
            forward(pillar_width)
            setheading(270)
            for stand_top in range(2):
                forward(short)
                left(90)
                forward(short)
                right(90)
            setheading(270)
            forward(long_height)
            setheading(180)
            for stand_bottom in range(2):
                forward(short)
                left(90)
                forward(short)
                right(90)
            end_fill()
            penup()

            for pillar_detail in range(2):
                goto(x + max_width/2 - short*(4 + pillar_detail*2),
                     y + max_height*floors + concrete + short*2)
                pendown()
                setheading(90)
                forward(long_height)
                penup()


            ## Draw the top concrete
            goto(x - max_width/2, y + max_height + max_height*floors - concrete)
            fillcolor('gray')
            begin_fill()
            pendown()
            setheading(0)
            for draw_concrete in range(2):
                forward(max_width)
                left(90)
                forward(concrete)
                left(90)
            end_fill()
            penup()

            ## Draw the tree
            gap = 20
            tree_height = 30
            tree_width = 20
            # Tree trunk
            goto(x - max_width/2 + pillar_width + gap,
                 y + max_height*floors + concrete)
            fillcolor('brown')
            begin_fill()
            pendown()
            setheading(90)
            forward(tree_height)
            setheading(0)
            forward(tree_width)
            setheading(270)
            forward(tree_height)
            end_fill()
            penup()
            # Tree leaves
            leaves = 20
            goto(x - max_width/2 + pillar_width + gap,
                 y + max_height*floors + concrete + tree_height)
            color("seagreen")
            dot(leaves)
            setheading(45)
            forward(leaves/2)
            dot(leaves*3/4)
            setheading(315)
            forward(leaves/2)
            dot(leaves)
            forward(leaves/2)
            dot(leaves/2)
            color('saddlebrown')

            ## Draw the fountain
            fountain_width = 40
            fountain_height = 10
            watering_width = 20
            watering_height = 30

            # Bottom part
            goto(x - fountain_width/2, y + max_height*floors + concrete)
            fillcolor('burlywood')
            begin_fill()
            pendown()
            setheading(90)
            forward(fountain_height)
            setheading(0)
            forward(fountain_width)
            setheading(270)
            forward(fountain_height)
            end_fill()
            penup()

            # Middle part
            goto(x + watering_width/2,
                 y + max_height*floors + concrete + fountain_height)
            fillcolor('beige')
            begin_fill()
            pendown()
            setheading(90)
            forward(watering_height/3)
            setheading(0)
            forward(watering_width/6)
            circle(watering_height/12, 180)
            forward(watering_width/6)
            setheading(90)
            forward(watering_height/6)
            setheading(0)
            forward(watering_width/6)
            circle(watering_height/12, 180)
            forward(watering_width/6)
            
            forward(watering_width)
            forward(watering_width/6)
            circle(watering_height/12, 180)
            forward(watering_width/6)
            setheading(270)
            forward(watering_height/6)
            setheading(180)
            forward(watering_width/6)
            circle(watering_height/12, 180)
            forward(watering_width/6)
            setheading(270)
            forward(watering_height/3)
            end_fill()
            penup()

            # Draw water
            water = 5
            pencolor('lightcyan')
            width(2)
            goto(x,
                 y + max_height*floors + concrete + fountain_height + watering_height)
            pendown()
            setheading(45)
            forward(water)
            setheading(0)
            forward(water*2)
            setheading(315)
            forward(water*2)
            setheading(270)
            forward(water*4)
            penup()

            goto(x,
                 y + max_height*floors + concrete + fountain_height + watering_height)
            pendown()
            setheading(135)
            forward(water)
            setheading(180)
            forward(water*2)
            setheading(225)
            forward(water*2)
            setheading(270)
            forward(water*4)
            penup()

            ## Draw bench
            bench_height = 20
            bench_width = 15
            goto(x + max_width/2 - pillar_width - gap,
                 y + max_height*floors + concrete)
            width(3)
            pencolor('maroon')
            pendown()
            setheading(90)
            forward(bench_height)
            setheading(270)
            forward(bench_height/2)
            setheading(180)
            forward(bench_width)
            setheading(270)
            forward(bench_height/2)
            penup()
            width(1)
            pencolor('saddlebrown')

    roof_width = max_width
    roof_height = max_height * num_floors

    ### Draw the under construction
    if 'X' in construction_finished:
        under_construction(x, y, roof_width, roof_height)

    ### Draw the roof
    elif 'O' in construction_finished:
        pass



###### Build City
def build_city(building_plan):
    for build in building_plan:
        building_style = 'none'
        if build[0] == 1:
            xcor = -225
            ycor = 0
        elif build[0] == 2:
            xcor = 25
            ycor = 0
        elif build[0] == 3:
            xcor = 275
            ycor = 0
        elif build[0] == 4:
            xcor = -375
            ycor = -25
        elif build[0] == 5:
            xcor = -125
            ycor = -25
        elif build[0] == 6:
            xcor = 125
            ycor = -25
        elif build[0] == 7:
            xcor = 375
            ycor = -25
        elif build[0] == 8:
            xcor = -275
            ycor = -50
        elif build[0] == 9:
            xcor = -25
            ycor = -50
        elif build[0] == 10:
            xcor = 225
            ycor = -50

        if 'A' in build[1]:
            building_A(xcor, ycor, build[2], build[3])
        elif 'B' in build[1]:
            building_B(xcor, ycor, build[2], build[3])
        elif 'C' in build[1]:
            building_C(xcor, ycor, build[2], build[3])
        elif 'D' in build[1]:
            building_D(xcor, ycor, build[2], build[3])
        


#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("The City of Soo Bin's World")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
fixed_plan_b = \
         [[1, 'C', 10, 'O'],
          [2, 'C', 9, 'O'],
          [3, 'C', 8, 'O'],
          [4, 'C', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'C', 5, 'O'],
          [7, 'C', 4, 'O'],
          [8, 'C', 3, 'O'],
          [9, 'C', 2, 'O'],
          [10, 'C', 1, 'O']]
fixed_plan_c = \
         [[1, 'C', 10, 'X'],
          [2, 'C', 9, 'X'],
          [3, 'C', 8, 'X'],
          [4, 'C', 7, 'X'],
          [5, 'C', 6, 'X'],
          [6, 'C', 5, 'X'],
          [7, 'C', 4, 'X'],
          [8, 'C', 3, 'X'],
          [9, 'C', 2, 'X'],
          [10, 'C', 1, 'X']]
fixed_plan_a = \
         [[1, 'A', 10, 'O'],
          [2, 'B', 9, 'O'],
          [3, 'C', 8, 'O'],
          [4, 'D', 7, 'O']]
fixed_plan_66 = \
        [[1, 'D', 9, 'O'],
         [2, 'B', 1, 'X'],
         [3, 'A', 6, 'X'],
         [4, 'B', 9, 'O'],
         [5, 'B', 3, 'O'],
         [6, 'A', 1, 'O'],
         [8, 'C', 10, 'O'],
         [10, 'B', 2, 'O']]
#build_city(fixed_plan_12) # <-- used for code development only, not marking
build_city(random_plan()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas(True)

#
#--------------------------------------------------------------------#

