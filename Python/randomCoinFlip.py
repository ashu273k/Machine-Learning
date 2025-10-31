import random
number_of_streaks = 0
experiments = 10000

def longest_streak(lst, value):
    max_streak = 0
    current_streak = 0
    for item in lst:
        if item == value:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 0

    return max_streak

for experiment_number in range(10000): # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    flips = []
    for i in range(100):
        flips.append(random.choice(['H', 'T']))
    
    # Code that checks if there is a streak of 6 heads or tails in a row
    streak_H = longest_streak(flips, 'H')
    streak_T = longest_streak(flips, 'T')
    if (streak_H >= 6 or streak_T >= 6):
        number_of_streaks += 1


print(f'Chance of streak: {(number_of_streaks / 100)}')
