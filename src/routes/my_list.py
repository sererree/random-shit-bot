from aiogram import Router
import asyncio
import random
my_list = ['Легче встать, когда не ложился.',
        'Если погонишься сразу за 2 зайцами, ни одной рыбы из пруда не поймаешь.',
           'Порой жизнь – всего лишь жизнь, а ты в ней – только порой.',
           'Заруби на лбу: бесплатные сыры раздают бесплатно!',
           'Удары в спину не пугают меня, за исключением, если спина моя.',
           'Учти, если не будешь стучать в дверь, она вряд ли откроется.']

i = random.randrange((len(my_list)))
print(my_list[i])