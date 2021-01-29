import time
import random

def bday():
    all_creators = ['my creator', 'father', 'dad', 'my lord', 'my king']
    all_wishes = ["a happy birthday. (geez, that's it)?", 'much success', 'good luck in every thing you do.', 'would stop with these jokes already...', 'would push that bug fix already', 'would patch my code already (YES, I SAID IT!)']
    
    creator = random.choice(all_creators)
    wish = random.choice(all_wishes)
    print('Happy birthday, %s! I wish you %s' % (creator, wish))

def blaze_it(extra=False):
    rollit = ["it's time.", "don't you have work to do?", 'STONKS!', 'funding secured!']
    print(random.choice(rollit))
    print('(p.s. they should really be paying you extra)')

def lol(imperialist=False):
    lolz = [('LOL' if not imperialist else "LOL (but in American)"), 'heehee', "this isn't even funny", 'this joke gets old real quick']
    print(random.choice(lolz))

def jmode():
    jokes = [
    'Programmer (noun.)\nA machine that turns coffee into code.',
    'What do you call a programmer from Finland?\nNerdic.',
    'You should ask your boss for arrays',
    'I used to C# but now I need glasses.',
    'Chuck Norris once got a return value from infinite recursion.',
    'Your code.',
    'Your code. (ouch!)',
'''
░░░░░░░▄▄▄▄▄▄░░░░░░░░░░░
░░░░░████▀▀███░░░░░░░░░░
░░░░███░░░░░▀██░░░░░░░░░
░░░░███▄░▄▄▄▄██░░░░░░░░░
░░░░████▀▀████▀░░░░░░░░░
░░░░██▄█▄▄░░░░░░░░░░░░░░
░░░░░████▄▄░░░░░░░░░░░░░
░░░░░░██▀░░▄█▄░░░░░░░░░░
░░░░░░████████▄░░░░░░░░░
░░░░░░█████████▄▄▄▄░░░░░
░░░░░▄████████████████▄▄
░░░▄████████████████████
▄███████████████████████
████████████████████████
████████████████████████
████████████████████████
████████████████████████
████████████████████████
████████████████████████
''',
    # LOL:
    '\a\a\a',
    '\a \aMust have been the wind...'
    ]

    print(random.choice(jokes))

def ny():
    resolutions = [
    'lose that extra weight...',
    'cancel that subscription.'
    'buy a sports car!',
    'become a rap star, yo. word is bond',
    'ask for a raise',
    'follow my dreams.',
    'get my shit together.',
    'get my shit together. like, seriously.'
    ]

    print('This year I will finally %s' % random.choice(resolutions))

def christ():
    lord_savior = [
    'Ho, ho, ho',
    'Merry Christmas!',
    "I see you've been... NAUGHTY",
    'Executing...\n> git commit\n> git push\n> git out && goto store\n> curl -X GET https://amzn.to/37JCPCU'
    ]
    
    print(random.choice(lord_savior))

def val():
    lord_savior = [
    'Better start swiping ;)',
    "Don't forget the wine!",
    'Checklist:\n-Wine\n-Flowers\n-Breath mints\n-Durex',
    'Heart Shaped Chocolates!!!'
    ]
    
    print(random.choice(lord_savior))


lt = time.localtime()
if lt.tm_mon == 2 and lt.tm_mday == 28:
    bday()

if lt.tm_mon == 2 and lt.tm_mday == 14:
    val()

if lt.tm_hour in (4, 16) and lt_tm_minute == 20:
    blaze_it(lt.tm_hour == 4)

if lt.tm_mday == 6 and lt.tm_mon == 9:
    lol()
    
if lt.tm_mday == 9 and lt.tm_mon == 6:
    lol(True)

if lt.tm_mday == 1 and lt.tm_mon == 1:
    ny()

if lt.tm_mday == 25 and lt.tm_mon == 12:
    christ()
