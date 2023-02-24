from tkinter import Button

# adding the cell class
class Cell:
    def __init__(self, is_mine=False):
        self.is_mine= is_mine
        self.cell_button_object = None

    def create_button_object(self,location):
        button= Button(
            location,
            text='Text'

        )
        # assign an event to a button
        # .bind uses two arguments, first being key that is clicked on button, second what functiont to be carried out.
        # Button-1 is left click according to tkinter
        button.bind('<Button-1>', self.left_click_actions )
        button.bind('<Button-3>', self.right_click_actions )
        self.cell_button_object= button

    # as per tkinter, need to add one more parameter for bind to occur succesfully
    def left_click_actions(self, event):
        print(event)
        print("Yo")
    
    def right_click_actions (self, event):
        print(event)
        print("Lol")