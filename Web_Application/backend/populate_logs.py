import datetime
import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smarttourist.settings')

import django

django.setup()

from collector.models import Log
from map.models import Place
from tourist.models import User as UserM

SEED = 0

places = {'nature':
                 [
                  '2',
'3',
'5',
'8',
'9',
'10',
'11',
'16',
'19',
'20',
'21',
'22',
'23',
'26',
'27',
'28',
'29',
'34',
'35',
'37',
'39',
'40',
'41',
'48',
'49',
'50',
'51',
'54',
'55',
'56',
'57',
'59',
'65',
'67',
'68',
'69',
'75',
'77',
'78',
'79',
'82',
'84',
'87',
'88',
'89',
'93',
'97',
'98',
'99',
'101',
'104'  
                ],
            'history': [
                    '1',
'4',
'6',
'7',
'8',
'12',
'13',
'14',
'15',
'17',
'18',
'21',
'22',
'23',
'25',
'27',
'30',
'31',
'32',
'33',
'36',
'42',
'43',
'44',
'45',
'46',
'47',
'49',
'50',
'51'
             ], 
            'religious': [
                '81',
'85',
'91',
'95',
'96',
'100',
'102',
'112',
'120',
'129',
'133',
'137',
'144',
'146',
'148',
'150',
'153',
'155',
'158',
'160',
'166',
'172',
'173',
'174',
'175',
'176',
'177',
'179',
'180',
'189',
'191',
'197',
'198',
'199',
'200',
'202',
'205',
'209',
'216',
'218',
'219',
'225',
'226',
'228',
'229',
'230',
'231',
'232',
'247',
'249',
'251',
'257',
'258',
'261',
'263',
'264',
'266',
'267',
'269',
'276',
'281',
'283',
'287',
'289',
'294',
'296',
'299',
'307',
'308',
'309',
'310',
'312'
            ]}

class User:
    userId = 0
    likes = {}
    events = {}

    def __init__(self, user_id, nature, history, religious):
        self.userId = user_id
        self.likes = {'nature': nature, 'history': history, 'religious': religious}

    def select_genre(self):
        return sample(self.likes)


def select_place(user):

    genre = user.select_genre()
    interested_places = places[genre]
    place_id = ''
    while place_id == '':
        place_candidate = interested_places[random.randint(0, len(interested_places) - 1)]
        place_id = place_candidate

    return place_id


def select_action(user):
    actions = {'genreView': 15, 'details': 50, 'moredetails': 24, 'addToList': 10, 'buy': 1}

    return sample(actions)


def sample(dictionary):
    random_number = random.randint(0, 100)
    index = 0
    for key, value in dictionary.items():
        index += value

        if random_number <= index:
            return key

def main():
    Log.objects.all().delete()
    random.seed(SEED)

    number_of_events = 100000

    print("Generating Data")
    users = [
        User(1, 20, 30, 50),
        User(2, 50, 20, 40),
        User(3, 20, 30, 50),
        User(4, 100, 0, 0),
        User(5, 0, 100, 0),
    ]
    print("Simulating " + str(len(users)) + " visitors")

    for x in range(0, number_of_events):
        randomuser_id = random.randint(0, len(users) - 1)
        user = users[randomuser_id]
        selected_place = select_place(user)
        print(selected_place)
        action = select_action(user)
        print("user id " + str(user.userId) + " selects place " + str(selected_place) + " and " + action)
        l = Log(user_id=UserM.objects.get(id=user.userId),
                content_id=Place.objects.get(id=selected_place),
                event=action,
                )
        l.save()

if __name__ == '__main__':
    print("Starting Place Log Population script...")
    main()
