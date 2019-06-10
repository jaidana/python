Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> postion
<function postion at 0x02E51F18>
>>> postion(femme)
['Pauline']
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> Dana in (femme)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Dana in (femme)
NameError: name 'Dana' is not defined
>>> 'Dana' in (femme)
True
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> 'Dana'._ _contains_ _('a')
SyntaxError: invalid syntax
>>> 'Dana'.__contains__('a')
True
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> Dana in contains()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Dana in contains()
NameError: name 'Dana' is not defined
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
Traceback (most recent call last):
  File "C:\Users\jayadana\Documents\dana's work\liste2.py", line 28, in <module>
    monConteneur
NameError: name 'monConteneur' is not defined
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> dana in MyContainer()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dana in MyContainer()
NameError: name 'dana' is not defined
>>> 'dana' in MyContainer()
True
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> len(MyContainer())
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    len(MyContainer())
TypeError: object of type 'MyContainer' has no len()
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> len(homme)
7
>>> femme __len__()
SyntaxError: invalid syntax
>>> femme.__len__()
6
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> card(femme)
[-1]
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> card(femme)
'Nadine'
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> card(femme)
['Dana', 'Mariyana', 'Pauline', 'Fatima', 'kathija', 'Nadine']
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> card(femme)
6
>>> len(femme)
6
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> card(femme)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    card(femme)
  File "C:\Users\jayadana\Documents\dana's work\liste2.py", line 37, in card
    return count(femme)
NameError: name 'count' is not defined
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> len(mySizeable)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    len(mySizeable)
TypeError: object of type 'type' has no len()
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> len(mySizeable())
18
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> 25 in MyContainer
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    25 in MyContainer
TypeError: argument of type 'type' is not iterable
>>> 25 inMyContainer()
SyntaxError: invalid syntax
>>> 25 in MyContainer()
True
>>> -96 in MyContainer()
True
>>> 
========== RESTART: C:\Users\jayadana\Documents\dana's work\pgcd.py ==========
11
>>> pgcd
<function pgcd at 0x00509660>
>>> pgcd()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    pgcd()
TypeError: pgcd() missing 2 required positional arguments: 'a' and 'b'
>>> 
========== RESTART: C:\Users\jayadana\Documents\dana's work\pgcd.py ==========
11
>>> 
========== RESTART: C:\Users\jayadana\Documents\dana's work\pgcd.py ==========
11 66
66 11
11
>>> 
========== RESTART: C:\Users\jayadana\Documents\dana's work\pgcd.py ==========
11 66
66 11
11
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> femme[1] = 'Toshimi'
>>> femme()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    femme()
TypeError: 'list' object is not callable
>>> femme
['Dana', 'Toshimi', 'Pauline', 'Fatima', 'kathija', 'Nadine']
>>> 
========= RESTART: C:\Users\jayadana\Documents\dana's work\liste2.py =========
>>> femme.__getitem__(2)
'Pauline'
>>> homme.__setitem__(1, 'Jacques')
>>> homme
['Jean', 'Jacques', 'Ghania', 'Jeremi', 'Mohammed', 'Ping', 'Geroge']
>>> 
