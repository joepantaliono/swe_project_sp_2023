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

def level_one():
    # Define the grid size
    grid_size = 10

    # Starting position of the two players
    player_1_pos = (0,0)
    player_2_pos = (grid_size - 1, grid_size -1)

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
        new_position = (new_position[0] % grid_size, new_position[1] % grid_size)
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

            # Printing out number of moves for the players
            print("The two players found each other after {} moves.".format(player1_moves + player2_moves))
            print("Player 1 made {} moves, and Player 2 made {} moves.".format(player1_moves, player2_moves))

            # Ask player if they want to play again
            play_again = input("Would you like to play again? (yes/no) ")
            if play_again.lower() != "yes":
                break

# Creates the game for grades 3-5
def level_two():
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
                player_positions.append(tuple([sum([pos[0] for pos in group])/len(group), sum([pos[1] for pos in group])/len(group)]))

    # Function to play the game.
    def play_game(rows, cols, num_players, player_positions):
        grid = build_grid(rows, cols)
        for i in range(num_players):
            row, col = map(int, input(f'Enter player {i+1} position (row, col): ').split())
            player_positions.append((row, col))
        moves = 0
        while len(player_positions) < num_players:
            moves += 1
            for i in range(num_players):
                direction = input(f'Player {i+1}, make a move (up, down, left, right): ')
                if direction == 'up':
                    player_positions[i] = (max(0, player_positions[i][0]-1, player_positions[i][1]))
                elif direction == 'down':
                    player_positions[i] = min(rows-1, player_positions[i][0]+1), player_positions[i][1]
                elif direction == 'left':
                    player_positions[i] = (player_positions[i][0], max(0, player_positions[i][1]-1))
                elif direction == 'right':
                    player_positions[i] = (player_positions[i][0], min(cols-1, player_positions[i][1]+1))
        check_group(player_positions)
        display_grid(grid, player_positions)

    # Function to calculate stats
    def calculate_stats(player_positions):
        distances = []
        for i in range(len(player_positions)-1):
            for j in range(i+1, len(player_positions)):
                distance = ((player_positions[i][0]-player_positions[j][0])**2 + (player_positions[i][1]-player_positions[j][1])**2)**0.5
                distances.append(distance)
        longest_run = max(distances) if distances else 0
        shortest_run = min(distances) if distances else 0
        average_run = sum(distances)/len(distances) if distances else 0
        return longest_run, shortest_run, average_run

    # Main function.
    def main():
        while True:
            rows, cols = map(int, input('Enter grid size (rows, cols): ').split())
            num_players = int(input('Enter the number of players (up to 4): '))
            player_positions = []
            play_game(rows, cols, num_players, player_positions)
            longest_run, shortest_run, average_run = calculate_stats(player_positions)
            print(f'\nGame finished in {len(player_positions)} moves.')
            print(f'Longest run without meeting: {longest_run:.2f}')
            print(f'Shortest run: {shortest_run:.2f}')
            print(f'Average run: {average_run:.2f}')
            replay = input('Do you want to play again? (yes or no): ')
            if replay != 'yes':
                break
    if __name__ == '__main__':
        main()
# Loop asking students which version of the game they want to play.
user = input("Select 1 for K-2 or 2 for 3-5: ")
if user == "1":
    level_one()
else:
    level_two()



