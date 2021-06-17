import random
for i in range(3):
    player = int(input('Enter the number: '))
    bot = random.randrange(1, 10)
    print(bot)
    if player == bot:
        print('You won!')
        break
    else:
        print('You lose!')