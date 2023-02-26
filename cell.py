from tkinter import Button, Label
import random
import settings

# adding the cell class
class Cell:
    # store instances in a list
    # append objects of the cell class to 'all'
    all = []

    cell_count = settings.CELL_COUNT

    # cell count is global
    cell_count_label_object = None


    def __init__(self, x, y, is_mine=False):
        self.is_mine= is_mine
        self.is_opened= False
        self.cell_button_object = None
        self.x= x
        self.y= y
        # append object to Cell.all list
        Cell.all.append(self)


    def create_button_object(self,location):
        button= Button(
            location,
            # increase size
            width=5,
            height=2,
        )

        # assign an event to a button
        # .bind uses two arguments, first being key that is clicked on button, second what functiont to be carried out.
        # Button-1 is left click according to tkinter
        button.bind('<Button-1>', self.left_click_actions )
        button.bind('<Button-3>', self.right_click_actions )
        self.cell_button_object= button
    
    @staticmethod
    # just for use case of the class, no for instance
    def create_cell_count_label(location):
        label= Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{Cell.cell_count}",
            font=("",20)
        )
        Cell.cell_count_label_object= label
    
        
    # as per tkinter, need to add one more parameter for bind to occur succesfully
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def get_cell_by_axis(self,x,y):
        # return cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    # seperated method, property to represent surrounded cells object
    # property is like an attribute which is read only
    # mark them as read only using a decorator     
    def surrounded_cells(self):
        # list include 8 surrounding cell objects
        surrounding_cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        # one-liner list comprehension to eliminate the 'none' values.
        surrounding_cells = [
            cell for cell in surrounding_cells if cell is not None
        ]

        return surrounding_cells
            
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_button_object.configure(text=self.surrounded_cells_mines_length)
            # replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                    )
        # mark the cell as opened
        self.is_opened = True
    
    def show_mine(self):
        # logic to interrupt the game and display player lost.
        self.cell_button_object.configure(bg='red')
    
    def right_click_actions (self, event):
        print(event)
        print("Lol")

    # static method to call from main.py after cell initiated
    # method- that doesn't belong each instance, belongs globally to class

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"