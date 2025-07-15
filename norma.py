from trans_codeeven import one_trans as o
from trans_codeodd import trans as t
from code_code import main
from code_code import per
import os
def result_code(): # Функция обрабатывает несколько передаваемых списков и соединяет их в одну строку <--> The function processes multiple passed lists and combines them into a single string
    p=[]
    for x in o():
        p.append(''.join(x))
    for x in t():
        p.append(''.join(x))
    return ''.join(p)
didnum=0
with open('codesresult.txt', 'w') as cd:  # Добавляет в отдельный файл хэшированный пароль(codesresult.txt можно заменить на свой файл) <--> Adds a hashed password to a separate file (codesresult.txt can be replaced with your own file)
    for _ in range(main()):
        didnum+=1
        password = result_code()          
        cd.write(f'{didnum}.Пароль: {''.join(next(per()))}\n Хэшированый пароль: {password[4:]}\n') 
