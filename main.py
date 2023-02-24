from tkinter import *
import settings
import utils

# initiate a window instance
# root is the variable, tk() being a regular window
root= Tk()
root.configure(bg="black") #setting background color


# adding attributes to make window nicer

# changing size of the window
# f'{}, using formatted string
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')

# changing the title
root.title("Minesweeper Game")
root.resizable(False, False) #To disable changing size of the window

# creating elements within window, dividing into multiple frames.
top_frame= Frame(
    root,
    bg='green',
    width=720,
    height=utils.height_percentage(25)
)

#locates the top frame, the top most left corner being 0,0
top_frame.place(x=0, y= 0)

left_frame= Frame(
    root,
    bg="black",
    width=utils.width_percentage(25),
    height=utils.height_percentage(75)
)

left_frame.place(x=0, y=utils.height_percentage(25))

center_frame= Frame(
    root,
    bg="blue",
    width=utils.width_percentage(75),
    height=utils.height_percentage(75)
)

center_frame.place(x=utils.width_percentage(25), y=utils.height_percentage(25))


# run tk until cross button is clicked
root.mainloop()