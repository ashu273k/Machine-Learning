import random
for i in range(100):
    flip = random.randint(0, 1)
    if flip == 0:
        print('H', end=' ')
    else:
        print('T', end=' ')
print()  # for a new line after the loop