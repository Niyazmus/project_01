# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random
print('Пункт А')
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
pop = random.sample(my_favorite_songs,3)

lpo = round(sum(_[1] for _ in pop),2 )

minut = int(str(lpo).split('.')[0])
sec = int(str(lpo).split('.')[1])

if int(sec) >= 60:
    sec -= 60
    print('Три песни звучат ', minut+1,'.', sec, ' минут',sep='')
else:
    print('Три песни звучат ', lpo, ' минут')

# Пункт D для А

import datetime
rrm = int(str(lpo).split('.')[0])
rrs = int(str(lpo).split('.')[1])

dt = datetime.timedelta(minutes=rrm, seconds=rrs)
print('\n   Пункт D для пункта А:   ', dt)

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

data = list(my_favorite_songs_dict.items())

r = random.sample(data, 3)
r = sum(i[1] for i in r)
r = float('{:.2f}'.format(r))

minut1 = int(str(r).split('.')[0])
sec1 = int(str(r).split('.')[1])

if int(sec) >= 60:
    sec -= 60
    print('\nПункт В''\nТри песни звучат ', minut1+1,'.', sec1, ' минут',sep='')
else:
    print('\nПункт В''\nТри песни звучат ', r, ' минут')

# Пункт D для В

import datetime
rrm1 = int(str(r).split('.')[0])
rrs1 = int(str(r).split('.')[1])
dt1 = datetime.timedelta(minutes=rrm1, seconds=rrs1)
print('\n   Пункт D для пункта B:   ', dt1)

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
