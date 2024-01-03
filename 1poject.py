# 1 уровень написать програму, которая переворачивает строку введеную пользователом
def reversed_user(user: str):
    join = ''.join(reversed(user))
    return join


# 1 уровень сумма чисел от 1 до 100 с остановкои по 10
def suma():
    num = 0
    for i in range(1,101):
        if i == 10:
            print(f"сумма 10 равна: {num}")
        elif i == 20:
            print(f"сумма 20 равна: {num}")
        if i == 30:
            print(f"сумма 30 равна: {num}")
        elif i == 40:
            print(f"сумма 40 равна: {num}")
        if i == 50:
            print(f"сумма 50 равна: {num}")
        elif i == 60:
            print(f"сумма 60 равна: {num}")
        if i == 70:
            print(f"сумма 70 равна: {num}")
        elif i == 80:
            print(f"сумма 80 равна: {num}")
        if i == 90:
            print(f"сумма 90 равна: {num}")
        elif i == 100:
            print(f"сумма 100 равна: {num}")
        num += i
    print(f'конец равень: {num}')


# 2 уровень сложности удалить дубликаты
def duplect(word: str):
    return set(word)


# 3 уровень надо зделать что бы проверался евляется ли слова полендромом и если надо игнорировать любые регистры
def polendrom(user: str):
    join = []
    koll = [",",'.','*','(',')','-','!','@','#','$','%','^','&','*','=','+',' ','{','}','[',']','<','>',';',':','?','/','`','~']
    for i in user:
        if i in koll:
            del i
        else:
            join.append(i)
    for j in range(len(user) // 2):
        if join[j] != join[-(j + 1)]:
            print('False')
        else:
            print('True')















