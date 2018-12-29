import random
import time
Coin = ['Head','Tail']
Head_results = 0
Tail_results = 0

while True:
    def flip_coin(Coin):
        print('Type flip to flip the coin and Type to see results results type ')
        response = input()
        if response =='flip':
            result = (random.choice(Coin))
            if result == 'Head':
                time.sleep(1)
                print('1...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('3...')
                time.sleep(1)
                print('Its a Head')
                global Head_results
                Head_results += 1
            if result == 'Tail':
                time.sleep(1)
                print('1...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('3...')
                time.sleep(1)
                print('Its a Tail')
                global Tail_results
                Tail_results += 1
        if response == 'results':
            print('Head results are - ' + str(Head_results))
            print('Tail results are - ' + str(Tail_results))



    flip_coin(Coin)
