#!/usr/bin/env python3
from pynput.keyboard import Key, Controller
import time
from sys import argv, exit
from progress.bar import IncrementalBar

keyboard = Controller()

latter_timeout = 0.2
enter_tab_timeout = 0.5

text = argv[1]
# timeaut = int(argv[2])

# text = str("AeVoqCEO21m1KZ\tpassword\n")

timeaut = 10
msg = f'The script is running!\nYou have {timeaut} seconds to put the cursor in the right place.'
print(msg)

bar = IncrementalBar('Countdown', max = timeaut)
for item in range(timeaut):
    bar.next()
    time.sleep(1)
                                                    
bar.finish()

def tab(letter):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(enter_tab_timeout)

def enter(letter):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(enter_tab_timeout)

def upper(letter):
    with keyboard.pressed(Key.shift):
        keyboard.press(letter)
        keyboard.release(letter)

for letter in text:
    time.sleep(latter_timeout)
    if letter.isspace():
        if letter == '\t': tab(letter)
        if letter == '\n': enter(letter)
    if letter.isupper(): upper(letter)
    else: keyboard.press(letter)
