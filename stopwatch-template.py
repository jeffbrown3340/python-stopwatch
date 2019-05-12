# template for "Stopwatch: The Game"
import simplegui
# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    return str(t)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    print "Start OK"
    
def stop_button():
    print "Stop OK"
    
def reset_button():
    print "Reset OK"

# define event handler for timer with 0.1 sec interval


# define draw handler


    
# create frame
swframe = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
swframe.add_button("Start",start_button)
swframe.add_button("Stop",stop_button)
swframe.add_button("Reset",reset_button)


# start frame
swframe.start()


# Please remember to review the grading rubric
