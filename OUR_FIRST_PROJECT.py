import random

def restaurant_choice(number):
    if number == 1:
        print("去吃949")
    elif number == 2:
        print("去吃豆腐锅")
    elif number == 3:
        print("去吃海底捞")
    elif number == 4:
        print("去吃麻辣烫")
    elif number == 5:
        print("去吃Phoholic")
    else:
        print("再想一想")

num = random.randint(1, 6)

restaurant_choice(num)