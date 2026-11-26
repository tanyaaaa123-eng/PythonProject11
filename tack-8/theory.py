from itertools import *
# формирует все возможные комбинации с повторениями
#буквы в алфавитном порядке
alph = sorted("")
# буквы в обратном порядке
aplh = sorted("",reverse=True)
for s in product("123",repeat=2):
    s = "".join(s) # объединяет все символы кортежа в строчку
for pos,s in enumerate(product("123",repeat=3),start = 1):
    print(s)
