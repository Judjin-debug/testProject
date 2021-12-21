import numpy as np
import math
import time


def time_decorator(func):
    
    def decorated_func(*args, **kwargs):
        
        a = time.time()
        result = func(*args, **kwargs)
        b = time.time()
        delta = b - a
        print(f'Function working time was {delta} seconds')
        return result
    
    return decorated_func


def random_predict(number:int=1) -> int:
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count
    
# print(f'Amount of tries:{random_predict()}')


@time_decorator
def score_game(random_predict) -> int:
    '''Mean average of 1000 tries of random_predict function to guess a number from 1 to 100
    
    Args:
      random_predict([type]): guessing function
      
    Returns:
      int: mean average of tries
    '''

    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Your algorithm guesses number in average for: {score} tries')
    return(score)


if __name__ == '__main__':
    score_game(random_predict)


# @time_decorator
# def score_game_v2(random_predict) -> int:
#     '''Mean average of 1000 tries of random_predict function to guess a number from 1 to 100
    
#     Args:
#       random_predict([type]): guessing function
      
#     Returns:
#       int: mean average of tries
#     '''
    
#     score = 0
#     # np.random.seed(1)
    
#     for i in range(1000):
#         score = (score + random_predict(np.random.randint(1, 101))) / 2
    
#     score = int(round(score, 0))
#     print(f'Your algorithm guesses number in average for: {score} tries')
#     return(score)

# score_game_v2(random_predict)