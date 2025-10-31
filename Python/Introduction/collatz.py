import sys
def collatz(number):
    
    if number % 2 == 0:
        number = number // 2
        print(number, end=' ')
    else:
        number = 3 * number + 1
        print(number, end=' ')
    if (number == 1):
        return 1
    collatz(number)


try:
    user_input = input('Enter a number: ')
    collatz(int(user_input))
    print()
    
except KeyboardInterrupt:
    sys.exit()