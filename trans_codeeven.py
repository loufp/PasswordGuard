from code_even import even  #Функция хэширует символы которые стоят на четных местах <--> The function hashes characters that are in even positions
from math import sqrt  # the square root <--> квадратный корень
from math import trunc  # the whole part <--> целая часть
from math import log10
from math import cbrt  # the cubic root <--> кубический корень
from even_alf_dictonary import sd1
from collections import OrderedDict
import random
def one_trans():
    irl=[]
    f = []
    alfabet='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for x in even():
        if x in alfabet:
            f.append(x)
    for o in even():
        try:
            def nerma():    #Тут обрабатываются цифры стоящие на четных местах <--> Numbers in even positions are processed here
                num=[]
                for prima in o:
                    p = str(round((log10(sqrt(cbrt(int(prima)))))+sqrt(2**log10(5)), 7)) #formula
                    ew=random.choice(['1','2','3','4','5','6','7','8','9'])
                    v=random.choice(['1','2','3','4','5','6','7','8','9'])
                    f = random.choice('qwertyuiop')
                    fj = random.choice('|!@#$%^&*~')
                    fq = random.choice('qwertyuiop!@#')
                    num.append((f'{f}{v}{fj}{p[5]}{fq}{ew}{ew}{v}'))
                return num
            irl.append(nerma())
        except:
            def two_trans(): #Тут обрабатываются буквы стоящие на четных местах <--> Letters in even positions are processed here
                alf=[]
                for voi in f:
                    if voi in sd1():
                        d=sd1()[f'{voi}']
                        alf.append(d)
                return alf
            irl.append(two_trans())
    
    return [list(item) for item in OrderedDict.fromkeys(tuple(item) for item in irl)]
