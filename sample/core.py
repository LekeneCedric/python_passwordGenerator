# -*- coding: utf-8 -*-
import random

def generate_custom_password(size:int,require)->str:
    siz = size
    res:str = ''
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    symbols = '@#$%&*/\?'
    data_use = lower_case+upper_case+number+symbols
    while siz > 0:
        for i2 in range(len(require)):
            if i2 == 0 :
                if require[i2]:
                    pos = random.randint(0,len(upper_case)-1)
                    charact = upper_case[pos]
                    res += charact
                    siz -=1
                else:
                    continue
            elif i2 == 1 :
                if require[i2]:
                    pos = random.randint(0,len(lower_case)-1)
                    charact = lower_case[pos]
                    res += charact
                    siz -=1
                else:
                    continue
            elif i2 == 2 :
                if require[i2]:
                    pos = random.randint(0,len(symbols)-1)
                    charact = symbols[pos]
                    res += charact
                    siz -=1
                else:
                    continue 
            elif i2 == 3 :
                if require[i2]: 
                    pos = random.randint(0,len(number)-1)
                    charact = number[pos]
                    res += charact
                    siz -=1
                else:
                    continue
            else :
                print("cas echeant")
                pos = random.randint(0,len(data_use)-1)
                charact = data_use[pos]
                res += charact
                siz -=1
    return res

def generate_simple_password(size:int)->str:
    res:str = ""
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    symbols = '@#$%&*/\?'
    data_use = lower_case+upper_case+number+symbols
    for i in range(size):
        res+= data_use[random.randint(0,len(data_use)-1)]
    return res