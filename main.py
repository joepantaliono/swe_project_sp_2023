from tkinter import *

def dynamicDataFrame(sim_data):
    data_frame = Frame(root, bg="white")
    # conditionally pick data
    if sim_data["num_players"] == 2:
        Label(data_frame, text="Number of players: " + str(sim_data["num_players"])).pack()
        Label(data_frame, text="Player 1 moves: " + str(sim_data["p1_move_count"])).pack()
        Label(data_frame, text="Player 2 moves: " + str(sim_data["p2_move_count"])).pack()
    elif sim_data["num_players"] == 3:
        Label(data_frame, text="Number of players: " + str(sim_data["num_players"])).pack()
        Label(data_frame, text="Player 1 moves: " + str(sim_data["p1_move_count"])).pack()
        Label(data_frame, text="Player 2 moves: " + str(sim_data["p2_move_count"])).pack()
        Label(data_frame, text="Player 3 moves: " + str(sim_data["p3_move_count"])).pack()
    elif sim_data["num_players"] == 4:
        Label(data_frame, text="Number of players: " + str(sim_data["num_players"])).pack()
        Label(data_frame, text="Player 1 moves: " + str(sim_data["p1_move_count"])).pack()
        Label(data_frame, text="Player 2 moves: " + str(sim_data["p2_move_count"])).pack()
        Label(data_frame, text="Player 3 moves: " + str(sim_data["p3_move_count"])).pack()
        Label(data_frame, text="Player 4 moves: " + str(sim_data["p4_move_count"])).pack()

    Label(data_frame, text="Grid size (x value): " + str(sim_data["grid_size_x"])).pack()
    Label(data_frame, text="Grid size (y value): " + str(sim_data["grid_size_y"])).pack()
    Button(data_frame, text="Reset", command = lambda : resetGame(data_frame)).pack()
    data_frame.pack()

def level_one():
    """grade k-2 logic here, return simulation output"""
    sim_data = {
        "num_players": 2,
        "p1_move_count": 0,
        "p2_move_count": 0
    }
    # only 2 players, just display 2 move counts
    data_frame = Frame(root, bg="white")
    Label(data_frame, text="Number of players: " + str(sim_data["num_players"])).pack()
    Label(data_frame, text="Player 1 moves: " + str(sim_data["p1_move_count"])).pack()
    Label(data_frame, text="Player 2 moves: " + str(sim_data["p2_move_count"])).pack()
    Button(data_frame, text="Reset", command = lambda : resetGame(data_frame)).pack()
    data_frame.pack()

def level_two():
    """grade 3-5 logic here, return simulation output"""
    sim_data = {
        "num_players": num_players.get(),
        "p1_move_count": 0,
        "p2_move_count": 0,
        "p3_move_count": 0,
        "p4_move_count": 0,
        "grid_size_x": 0,
        "grid_size_y": 0,
    }
    dynamicDataFrame(sim_data)

def level_three():
    """grade 6-8 logic here, return simulation output"""
    sim_data = {
        "num_players": num_players.get(),
        "p1_move_count": 0,
        "p2_move_count": 0,
        "p3_move_count": 0,
        "p4_move_count": 0,
        "grid_size_x": 0,
        "grid_size_y": 0,
    }
    # experiements, different protocols for moving
    dynamicDataFrame(sim_data)

def resetGame(data_frame):
    """send player back to choose grade level and players"""
    data_frame.forget()
    submit_button.pack()

def gradeCallback():
    submit_button.forget()
    """Called when user selects grade (initial screen)
    StringVar: grade.get()"""
    # print('Grade is ' + grade.get())
    # determine simulation function
    if grade.get() == "K-2":
        level_one()
    elif grade.get() == "3-5":
        level_two()
    elif grade.get() == "6-8":
        level_three()

root = Tk() # serves as main window of application
root.geometry("800x800")

num_players=IntVar()

select_grade_frame = Frame(root, bg="white")
grade = StringVar() # variable holding selected grade
# grade.set('')
Label(select_grade_frame, text="Wandering in the Woods Game").pack()

Radiobutton(select_grade_frame, text='Grades K-2', value='K-2', variable=grade).pack()

Radiobutton(select_grade_frame, text='Grades 3-5', value='3-5', variable=grade).pack()
Label(select_grade_frame, text="Players: ").pack()
Entry(select_grade_frame,textvariable=num_players).pack()

Radiobutton(select_grade_frame, text='Grades 6-8', value='6-8', variable=grade).pack()
Label(select_grade_frame, text="Players: ").pack()
Entry(select_grade_frame,textvariable=num_players).pack()

submit_button = Button(select_grade_frame, text="Let's go!", command=gradeCallback)
submit_button.pack()
submit_button["command"] = gradeCallback

select_grade_frame.pack()
# quit_button= Button(root, text="Quit", command=root.destroy)

root.mainloop() # responds to user input until program terminates