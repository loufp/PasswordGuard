from code_code import per
def odd(): #Selects symbols that are in odd positions <--> Отбирает символы которые стоят на нечетных местах
    n=[]
    l=0
    if len(''.join(next(per())))%2==0:
        for x in ''.join(next(per())):
            l+=1
            if l%2!=0:
                n.append(x)
    return n
