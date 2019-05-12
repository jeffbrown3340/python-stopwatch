# JLB 6-19-15
# http://www.codeskulptor.org/#user40_GpQl46Vzhr_11.py

# template for "Stopwatch: The Game"

import simplegui
import math
import time

# define global variables
t = 0
status_message_xpos = 35
status_message = ""
points = 0
tries = 0
max_tries = 5

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    # t is count of tenths of seconds
    # calculate remainder tenths, which is the ones position
    tenths = t % 10

    # take away the tenths, divide by tenths per minute (10*60) rounded down
    # coercing to int for display purposes in the string build
    minutes = int(math.floor((t - tenths)/(10 * 60)))

    # take away minutes and tenths, remainder is secs * 10 centisec/sec
    seconds = int((t - (minutes * 60 * 10) - tenths) / 10)

    # build the returned string from right to left
    string_to_return = "." + str(tenths) #decimal point and tenths
    string_to_return = str(seconds) + string_to_return #seconds
    if seconds < 10:
        string_to_return = "0" + string_to_return # pad zero to single digit
    string_to_return = ":" + string_to_return
    string_to_return = str(minutes) + string_to_return
    return string_to_return
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global t, status_message, status_message_xpos
    if tries >= max_tries:
        status_message_xpos = 65
        status_message = "Game over, hit Reset."
    else:
        timer.start()
        status_message = ""
    
def stop_button():
    global t, tries, points, status_message, status_message_xpos
    if timer.is_running():
        timer.stop()
        tries += 1
        status_message_xpos = 75
        if t % 10 == 0:
            points += 1
            status_message = "You scored a point!"
        else:
            if tries >= max_tries:
                status_message_xpos = 30
                status_message = "Oops! Game over, hit Reset."
            else:
                status_message_xpos = 75
                status_message = "Oops ... try Again."
    
def reset_button():
    global t, tries, points, status_message
    timer.stop()
    t = 0
    tries = 0
    points = 0
    status_message = ""

# define event handler for timer with 0.1 sec interval
def timer_event_handler():
    global t
    t += 1
    # reset to zero after 9:59.9
    if t > (10 * 60 * 10) - 1:
        t = 0
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(points) + "/" + str(tries), [250,25], 24, "Yellow")
    canvas.draw_text(format(t), [100,112], 48, "White")
    canvas.draw_text(status_message, [status_message_xpos,190], 24, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 325, 200)
timer = simplegui.create_timer(100, timer_event_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start",start_button)
frame.add_button("Stop",stop_button)
frame.add_button("Reset",reset_button)

# start frame
frame.start()
