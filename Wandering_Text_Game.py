""""
Wandering in the Woods game
Spring 2023-Final Project
Benjamin Gorgan - benjaminrgorgan@lewisu.edu
Eugene Henneberry - eugenethenneberry@lewisu.edu
Kyle Bowler - KyleBowler@lewisu.edu
Joseph Pantaliono
Francis Sumayop
CPSC-44000-Software Engineering - Spring '23
March 3, 2023,
Simulation of a game allowing students to select
the appropriate level and interact with the simulation
"""
import random

# Creates game for grades K-2
def sim_one():
    sim_data = {
        "num_players": 2,
        "p1_move_count": 0,
        "p2_move_count": 0
    }
    # Define the grid size
    grid_size = 10

    # Starting position of the two players
    player_1_pos = (0, 0)
    player_2_pos = (grid_size - 1, grid_size - 1)

    # Counter for players moves
    player1_moves = 0
    player2_moves = 0

    def move_players(player_pos):
        # Creates random direction
        direction = random.choice(['up', 'down', 'left', 'right'])

        # Updates the players position
        if direction == 'up':
            new_position = (player_pos[0], player_pos[1] - 1)
        elif direction == 'down':
            new_position = (player_pos[0], player_pos[1] + 1)
        elif direction == 'left':
            new_position = (player_pos[0] - 1, player_pos[1])
        elif direction == 'right':
            new_position = (player_pos[0] + 1, player_pos[1])

        # If the new position is out of the grid move to the other side of the grid.
        new_position = (new_position[0] %
                        grid_size, new_position[1] % grid_size)
        return new_position

    #
    # Define the find function
    def check_find(player_1, player_2):
        return player_1 == player_2

        # Main loop

    while True:
        # Reset the players
        player_1 = player_1_pos
        player_2 = player_2_pos
        player1_moves = 0
        player2_moves = 0

        # Loop untill the players find each other
        while not check_find(player_1, player_2):
            player_1 = move_players(player_1_pos)
            player1_moves += 1
            player_2 = move_players(player_2)
            player2_moves += 1
        
        sim_data["p1_move_count"] = player1_moves
        sim_data["p2_move_count"] = player1_moves
        return sim_data

# Creates game for grades 3-5.
def level_two():
    # Function to build the grid
    def build_grid(size):
        grid = []
        for row in range(size):
            grid.append([])
            for colum in range(size):
                grid[row].append('.')
        return grid

    def get_players():
        while True:
            try:
                num_players = int(input("How many players? (1-4): "))
                if num_players <= 1 or num_players > 4:
                    print("Invalid number of players.")
                else:
                    return num_players
            except ValueError:
                print("Invalid input. Please enter a number 1-4")

    def starting_positions(num_players, size):
        positions = []
        for i in range(num_players):
            while True:
                try:
                    row = int(input(f"Enter the row for player {i + 1}: "))
                    column = int(
                        input(f"Enter the column for player {i + 1}: "))
                    if row < 0 or row >= size or column < 0 or column >= size:
                        print(
                            "Invalid position. Please choose a position within the grid.")
                    elif (row, column) in positions:
                        print(
                            "Position already taken. Please choose a different position.")
                    else:
                        positions.append((row, column))
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        return positions

    def adjacent(pos_1, pos_2):
        row_1, col_1 = pos_1
        row_2, col_2 = pos_2
        if abs(row_1 - row_2) <= 1 and abs(col_1 - col_2) <= 1:
            return True
        return False

    # Function to play the game.
    def play_game(grid, positions):
        num_players = len(positions)
        moves = [0] * num_players
        found = [False] * num_players
        moves_to_find = [0] * num_players

        while not all(found):
            for i in range(num_players):
                if not found[i]:
                    moves[i] += 1
                    row, column = positions[i]
                    direction = random.choice(['up', 'down', 'left', 'right'])
                    if direction == 'up':
                        if row > 0:
                            row -= 1
                    elif direction == 'down':
                        if row < len(grid) - 1:
                            row += 1
                    elif direction == 'left':
                        if column > 0:
                            column -= 1
                    elif direction == 'right':
                        if column < len(grid[0]) - 1:
                            column += 1
                    positions[i] = (row, column)

                    for j in range(num_players):
                        if not found[j] and i != j and adjacent(positions[i], positions[j]):
                            found[j] = True
                            found[i] = True
                            moves_to_find[j] = moves[i]

                    if all(found):
                        break

            if found.count(False) == 1:
                remaining_player = found.index(False)
                for i in range(num_players):
                    if i != remaining_player:
                        row_dir = 1 if positions[remaining_player][0] < positions[i][0] else -1
                        col_dir = 1 if positions[remaining_player][1] < positions[i][1] else -1

                        while not adjacent(positions[remaining_player], positions[i]):
                            row, col = positions[remaining_player]
                            if abs(row - positions[i][0]) > abs(col - positions[i][1]):
                                row += row_dir
                            else:
                                col += col_dir
                            positions[remaining_player] = (row, col)
                            moves[remaining_player] += 1

                        found[remaining_player] = True
                        moves_to_find[remaining_player] = moves[i]

                        break
        print("Game Over!")
        for i in range(num_players):
            print(
                f"Player {i + 1}: {moves[i]}, {moves_to_find[i]} moves to find.")
        print()

    # Main game loop
    while True:
        size = int(input("What is the grid size? "))
        num_players = get_players()
        positions = starting_positions(num_players, size)
        grid = build_grid(size)

        # Place players on the grid
        for i, position in enumerate(positions):
            row, column = position
            grid[row][column] = str(i+1)

        print("Starting positions:")
        for row in grid:
            print(" ".join(row))

        play_game(grid, positions)

        replay = input("Would you like to play again? (y/n) ")
        if replay.lower() != 'y':
            break


# Creates the game for grades 6-8
def level_three():
    # Function to build the grid
    def build_grid(rows, cols):
        return [['.' for j in range(cols)] for i in range(rows)]

    # Function to display the grid with player positions
    def display_grid(grid, player_position):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in player_position:
                    print('P', end='')
                else:
                    print(grid[i][j], end='')
            print()
    # Function to check if two or more players found each other

    def check_group(player_positions):
        groups = []
        for i in range(len(player_positions)):
            group_found = False
            for group in groups:
                if player_positions[i] in group:
                    group.append(player_positions[i])
                    group_found = True
                    break
            if not group_found:
                groups.append([player_positions[i]])
        for group in groups:
            if len(group) > 1:
                for pos in group:
                    player_positions.remove(pos)
                player_positions.append(tuple(
                    [sum([pos[0] for pos in group])/len(group), sum([pos[1] for pos in group])/len(group)]))

    # Function to play the game.
    def play_game(rows, cols, num_players, player_positions):
        grid = build_grid(rows, cols)
        for i in range(num_players):
            row, col = map(int, input(
                f'Enter player {i+1} position (row, col): ').split())
            player_positions.append((row, col))
        moves = 0
        while len(player_positions) < num_players:
            moves += 1
            for i in range(num_players):
                direction = input(
                    f'Player {i+1}, make a move (up, down, left, right): ')
                if direction == 'up':
                    player_positions[i] = (
                        max(0, player_positions[i][0]-1, player_positions[i][1]))
                elif direction == 'down':
                    player_positions[i] = min(
                        rows-1, player_positions[i][0]+1), player_positions[i][1]
                elif direction == 'left':
                    player_positions[i] = (
                        player_positions[i][0], max(0, player_positions[i][1]-1))
                elif direction == 'right':
                    player_positions[i] = (player_positions[i][0], min(
                        cols-1, player_positions[i][1]+1))
        check_group(player_positions)
        display_grid(grid, player_positions)

    # Function to calculate stats
    def calculate_stats(player_positions):
        distances = []
        for i in range(len(player_positions)-1):
            for j in range(i+1, len(player_positions)):
                distance = ((player_positions[i][0]-player_positions[j][0])**2 + (
                    player_positions[i][1]-player_positions[j][1])**2)**0.5
                distances.append(distance)
        longest_run = max(distances) if distances else 0
        shortest_run = min(distances) if distances else 0
        average_run = sum(distances)/len(distances) if distances else 0
        return longest_run, shortest_run, average_run

    # Main function.
    def main():
        while True:
            rows, cols = map(int, input(
                'Enter grid size (rows, cols): ').split())
            num_players = int(input('Enter the number of players (up to 4): '))
            player_positions = []
            play_game(rows, cols, num_players, player_positions)
            longest_run, shortest_run, average_run = calculate_stats(
                player_positions)
            print(f'\nGame finished in {len(player_positions)} moves.')
            print(f'Longest run without meeting: {longest_run:.2f}')
            print(f'Shortest run: {shortest_run:.2f}')
            print(f'Average run: {average_run:.2f}')
            replay = input('Do you want to play again? (yes or no): ')
            if replay != 'yes':
                break
    if __name__ == '__main__':
        main()
