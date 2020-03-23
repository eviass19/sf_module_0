import random

x=1
y=100

def bsearch(number,guess,x,y):
    count=1
    if x>y:
        return False
    else:
        mid=(x+y)//2
        if number==mid:
            count+=1
            return mid
        elif number<mid:
            return bsearch(number,guess,x,mid-1)
            count+=1
        else:
            return bsearch(number,guess,mid+1,y)
            count+=1
        

guess=random.randint(x,y)       

number=random.randint(1,100)


s=bsearch(number,guess,x,y)

if s==False:
    print('Not relevant number')
else:
    print('Number is', s, ' Qty of trials is', count)

def score_game(bsearch):
    #'''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 100, size=(1000))
    for i in random_array:
        count_ls.append(count)
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
 
score_game(bsearch)
