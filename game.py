import numpy as np

import sys

print(sys.version)

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100\n'))
    
    if predict_number < number:
        print('Number should be greater')
        
    elif predict_number > number:
        print('Number should be smaller')
        
    else:
        print(f'You\'ve guessed the number! This number = {number}, for {count} tries')
        break