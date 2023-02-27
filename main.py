from tkinter import *

def gradeCallback():
    """called when user picks grade"""
    print('Grade is ' + grade.get())

def level_one():
    """grade k-2 logic SIMULATION here, return simulation output"""
    pass

def level_two():
    """grade 3-5 logic SIMULATION here, return simulation output"""
    pass

def level_three():
    """grade 6-8 logic SIMULATION here, return simulation output"""
    pass

root = Tk() # serves as main window of application
root.geometry("800x800")

starting_info = Frame(root, bg="white") # FRAME is child of root, holds elements
grade = StringVar() # selected grade variable
grade.set('')
Label(starting_info, text="Wandering in the Woods Game").pack()
Radiobutton(starting_info, text='Grades K-2', value='K-2', variable=grade).pack()
Radiobutton(starting_info, text='Grades 3-5', value='3-5', variable=grade).pack()
Radiobutton(starting_info, text='Grades 6-8', value='6-8', variable=grade).pack()
grade_label = Label(starting_info, textvariable=grade, text=grade).pack()
submit_button = Button(starting_info, text="Let's go!")
submit_button.pack()
submit_button["command"] = gradeCallback
starting_info.pack()

# ttk.Label(starting_info, text="Kyle Bowler, Benjamin Gorgan, Eugene Henneberry, Joseph Pantaliono, Francis Sumayop").pack(column=0, row=0)

Button(root, text="Quit", command=root.destroy).pack()

root.mainloop() # responds to user input until program terminates