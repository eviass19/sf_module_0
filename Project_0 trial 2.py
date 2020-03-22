import random
import numpy as np


def bsearch(number,guess,x,y):    
    count=1 #counter
    if x>y: 
        return False
    else:
        mid=(x+y)//2  #Indicating the center of the array
        if number==mid:
            count+=1
            return mid
        elif number<mid:
            return bsearch(number,guess,x,mid-1) # Changing the the greater border of the array
            count+=1
        else:
            return bsearch(number,guess,mid+1,y)  # Changing the the lower border of the array
            count+=1
        
guess=np.random.randint(x,y)       #Guessing the number
x=1 
y=100
number=np.random.randint(1,100)   #The secret number 


s=bsearch(number,guess,x,y)

if s!=False:
    print('Number is', s, ' Qty of trials is', count)
else:
    print('Not relevant number')

    
def score_game(bsearch):
    #'''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 100, size=(1000))
    for i in random_array:
        count_ls.append(bsearch(number,my_list,x,y))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
 
score_game(bsearch)

