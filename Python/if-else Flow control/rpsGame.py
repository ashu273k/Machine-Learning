import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    while True: # The main game loop
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        player_move = input('>')

        if player_move == 'q':
            sys.exit()  # Quit the program
        if player_move in ['r', 'p', 's']:
            break # Valid move, break out of the loop
        print('Invalid move. Please try again and type "r", "p", or "s".')
    
    # Display what the player chose
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')
    
    # Display what the computer chose
    computer_move = random.choice(['r', 'p', 's'])
    if computer_move == 'r':
        print('ROCK')
    elif computer_move == 'p':
        print('PAPER')
    elif computer_move == 's':
        print('SCISSORS')

    # Display and record the win/loss/tie
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or \
 (player_move == 'p' and computer_move == 'r') or \
         (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1
