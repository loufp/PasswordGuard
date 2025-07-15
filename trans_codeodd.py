from code_odd import odd #  Функция хэширует символы которые стоят на нечетных местах <--> The function hashes characters that are in odd positions
from math import sqrt,trunc,log,cbrt
import random
from odd_alf_dictonary import sd2
from collections import OrderedDict
def trans(): 
    lita=[]
    fl = []
    alfabet='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for x in odd():
        if x in alfabet:
            fl.append(x)
    for o in odd():
        try:
            def odis_code(): #Тут обрабатываются цифры стоящие на нечетных местах <--> Numbers in odd positions are processed here
                odd_code=[]
                for x in o:
                    mh=log((int(x)+sqrt(5)*trunc(cbrt(4*int(x)))),3)
                    mh=str(mh)
                    r=random.randint(1,5)
                    xl=random.choice(['!','@','$','(','#','_','@','|','>','<','?','~'])
                    xl2=random.choice(['ᚢ','ᚦ','ᚨ','ᚱ','ᚲ','ᚷ','ᚹ','ᛃ','ᛇ','ᛈ','ᛉ','ᛊ','ᛏ','ᛒ','ᛖ','ᛗ','ᛚ','ᛜ','ᛟ','ᛞ','🔒','🔑','🗝️','✉️','📜'])
                    xl3=random.choice(['ᚢ','ᚦ','ᚨ','ᚱ','ᚲ','ᚷ','ᚹ','ᛃ','ᛇ','ᛈ','ᛉ','ᛊ','ᛏ','ᛒ','ᛖ','ᛗ','ᛚ','ᛜ','ᛟ','ᛞ','🔒','🔑','🗝️','✉️','📜'])
                    xl4=random.choice(['⌘','⏎','⚠','✦','✧','♔','♕','♖'])
                    xl5=random.choice(['⌘','⏎','⚠','✦','✧','♔','♕','♖'])
                    mm=random.randint(10,52)
                    mm1=random.randint(10,42)
                    mm2=random.randint(100,322)
                    mm3=random.randint(10,22)
                    odd_code.append((f'{mm1}{xl}{xl5}{mm2}{xl2}{r}{mh[5]}{mm3}{xl4}{r}{xl3}{xl4}{mm}'))
                return odd_code
            lita.append(odis_code())
        except:
            def transver():#Тут обрабатываются буквы стоящие на нечетных местах <--> Letters in odd positions are processed here
                we=[]
                for voi in fl:
                    if voi in sd2():
                        d=sd2()[f'{voi}']
                        we.append(d)
                return we
            lita.append(transver())
            
    return [list(item) for item in OrderedDict.fromkeys(tuple(item) for item in lita)]
