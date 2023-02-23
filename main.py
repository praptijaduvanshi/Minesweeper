from tkinter import *

# initiate a window instance
# root is the variable, tk() being a regular window
root= Tk()
root.configure(bg="green") #setting background color


# adding attributes to make window nicer

# changing size of the window
root.geometry('720x360')

# changing the title
root.title("Minesweeper Game")
root.resizable(False, False) #To disable changing size of the window




# run tk until cross button is clicked
root.mainloop()