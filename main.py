#!/usr/bin/env python3
from pynput.keyboard import Key, Controller
import time
from sys import argv, exit
from progress.bar import IncrementalBar

keyboard = Controller()

text = argv[1]
timeaut = int(argv[2])

# text = "AeVoqCEO21m1KZ"
# timeaut = 10
msg = f'The script is running!\nYou have {timeaut} seconds to put the cursor in the right place.'
print(msg)

bar = IncrementalBar('Countdown', max = timeaut)
for item in range(timeaut):
    bar.next()
    time.sleep(1)

bar.finish()

# keyboard.type(text)
for letter in text:
    if letter.isupper():
        with keyboard.pressed(Key.shift):
            keyboard.press(letter)
            keyboard.release(letter)
    else:
        keyboard.press(letter)
        keyboard.release(letter)


