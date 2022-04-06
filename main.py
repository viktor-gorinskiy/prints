#!/usr/bin/env python3
from pynput.keyboard import Key, Controller
import time
from sys import argv, exit
from progress.bar import IncrementalBar

keyboard = Controller()

latter_timeout = 0
enter_tab_timeout = 0.1

try:
    text = str(argv[1])
except IndexError:
    msg = r'prints "login\tpassword"' + '\n\tOR any string\n' + r'prints "daipeisichiN2ahkoh1eg3uwaaquah"'
    print(msg)
    # print('prints "login"\tpassword\n\tOR\nprints "daipeisichiN2ahkoh1eg3uwaaquah"')
    exit(1)
text = '\t'.join(text.split(r'\t'))
text = '\n'.join(text.split(r'\n'))

timeaut = 15
try:
    timeaut = int(argv[2])
except IndexError:
    msg = 'The timeout has not been set, by default it will be 15 seconds!'
    print(msg)
except ValueError:
    msg = 'The timeout must be a number and equal to the number of seconds!\n EXIT'
    print(msg)
    exit(1)

if len(argv) >= 4:
    latter_timeout = int(argv[3])
    print('latter_timeout ==', latter_timeout)

if len(argv) == 5:
    enter_tab_timeout = int(argv[4])
    print('enter_tab_timeout ==', enter_tab_timeout)

def sleep_bar(second):
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

sleep_bar(timeaut)

for letter in text:
    time.sleep(latter_timeout)
    if letter.isspace():
        if letter == '\t': tab(letter)
        if letter == '\n': enter(letter)
    if letter.isupper(): upper(letter)
    else: keyboard.press(letter)


