#!/usr/bin/env python3
# coding=utf-8
#
# shuffle-romaji.py
# v1.0
#
# Shuffles a built-in list of Japanese Romaji
#   and presents them one character at a time.
#
# Useful when testing your knowledge of Hiragana.
#   (Draw the corresponding Hiragana from memory.)

import random
import signal
import sys

# Magic for nicely quitting on CTRL+C
# http://stackoverflow.com/a/1112350/7351717
def signal_handler(signal, frame):
    print('Received SIGINT!  Exiting...')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# http://www.freejapaneselessons.com/lesson01.cfm
hiragana = {
    'a': 'あ',
    'i': 'い',
    'u': 'う',
    'e': 'え',
    'o': 'お',
    'ka': 'か',
    'ki': 'き',
    'ku': 'く',
    'ke': 'け',
    'ko': 'こ',
    'ga': 'が',
    'gi': 'ぎ',
    'gu': 'ぐ',
    'ge': 'げ',
    'go': 'ご',
    'sa': 'さ',
    'shi': 'し',
    'su': 'す',
    'se': 'せ',
    'so': 'そ',
    'za': 'ざ',
    'ji': 'じ',
    'zu': 'ず',
    'ze': 'ぜ',
    'zo': 'ぞ',
    'ta': 'た',
    'chi': 'ち',
    'tsu': 'つ',
    'te': 'て',
    'to': 'と',
    'da': 'だ',
    'ji (rare)': 'ぢ',
    'zu (rare)': 'づ',
    'de': 'で',
    'do': 'ど',
    'na': 'な',
    'ni': 'に',
    'nu': 'ぬ',
    'ne': 'ね',
    'no': 'の',
    'ha (wa)': 'は',
    'hi': 'ひ',
    'fu': 'ふ',
    'he (e)': 'へ',
    'ho': 'ほ',
    'ba': 'ば',
    'bi': 'び',
    'bu': 'ぶ',
    'be': 'べ',
    'bo': 'ぼ',
    'pa': 'ぱ',
    'pi': 'ぴ',
    'pu': 'ぷ',
    'pe': 'ぺ',
    'po': 'ぽ',
    'ma': 'ま',
    'mi': 'み',
    'mu': 'む',
    'me': 'め',
    'mo': 'も',
    'ya': 'や',
    'yu': 'ゆ',
    'yo': 'よ',
    'ra': 'ら',
    'ri': 'り',
    'ru': 'る',
    're': 'れ',
    'ro': 'ろ',
    'wa': 'わ',
    'wo': 'を',
    'n/m': 'ん',
    'kya': 'きゃ',
    'kyu': 'きゅ',
    'kyo': 'きょ',
    'gya': 'ぎゃ',
    'gyu': 'ぎゅ',
    'gyo': 'ぎょ',
    'sha': 'しゃ',
    'shu': 'しゅ',
    'sho': 'しょ',
    'ja': 'じゃ',
    'ju': 'じゅ',
    'jo': 'じょ',
    'cha': 'ちゃ',
    'chu': 'ちゅ',
    'cho': 'ちょ',
    'nya': 'にゃ',
    'nyu': 'にゅ',
    'nyo': 'にょ',
    'hya': 'ひゃ',
    'hyu': 'ひゅ',
    'hyo': 'ひょ',
    'bya': 'びゃ',
    'byu': 'びゅ',
    'byo': 'びょ',
    'pya': 'ぴゃ',
    'pyu': 'ぴゅ',
    'pyo': 'ぴょ',
    'mya': 'みゃ',
    'myu': 'みゅ',
    'myo': 'みょ',
    'rya': 'りゃ',
    'ryu': 'りゅ',
    'ryo': 'りょ'
    }

romaji = sorted(hiragana.keys())
random.shuffle(romaji)

print("See if you can draw the Hiragana!")
print("(Hint:  Press ENTER to continue.)\n")

for item in romaji:
    fancycounter = ("[" + str(romaji.index(item)+1).zfill(3) +
               "/" + str(len(romaji)) + "]")
    print(fancycounter + " ", end='')
    print(item, end='')
    input()
    print(fancycounter + " ", end='')
    print(hiragana[item], end='\n\n')
    
print("That is all of them!")
print("Press ENTER to exit.", end='')
input()
