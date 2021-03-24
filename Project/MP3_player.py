import os
from playsound import playsound
import random
import inquirer

qq = os.listdir(os.path.join(os.path.dirname(__file__), 'Music'))


music_pl=[]
for i in range(len(qq)):
    if qq[i].endswith('.wav'):
        music_pl.append(qq[i])
music_pl.append('Shuffle')


questions = [
    inquirer.List('size',
                message='what do you want to listen?',
                choices=music_pl
    ),
]
answers = inquirer.prompt(questions)


if answers['size'] == 'Shuffle':
    music_pl_1 = music_pl[:-1]
    random.shuffle(music_pl_1)
    for i in music_pl_1:
        playsound(f'Music/{i}')
else:
    playsound(f"Music/{answers['size']}")