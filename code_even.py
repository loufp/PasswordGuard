from code_code import per
def even(): # Selects symbols that are in even positions <--> Отбирает символы которые стоят на четных местах
    e=[]
    l=0
    if len(''.join(next(per())))%2==0:
        for x in ''.join(next(per())):
            l+=1
            if l%2==0:
                e.append(x)
                
    return e
