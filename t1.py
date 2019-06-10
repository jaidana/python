Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:/Users/jayadana/Documents/dana's work/tuple.py =========
>>> p.x
3
>>> p.y
5
>>> p[0]
3
>>> p
Point2D(x=3, y=5)
>>> 
========= RESTART: C:/Users/jayadana/Documents/dana's work/deque.py =========
>>> d
deque(['a', 'b', 'c'])
>>> 
========= RESTART: C:/Users/jayadana/Documents/dana's work/deque.py =========
>>> d.appendleft('dana')
>>> d.append('lakshmi')
>>> d
deque(['dana', 'a', 'b', 'c', 'lakshmi'])
>>> 
========= RESTART: C:/Users/jayadana/Documents/dana's work/deque.py =========
>>> d.popleft()
'a'
>>> d.popleft()
'b'
>>> d.extendleft(['b','a'])
>>> d
deque(['a', 'b', 'c'])
>>> d.append('e', 'f', 'g')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d.append('e', 'f', 'g')
TypeError: append() takes exactly one argument (3 given)
>>> d.append('e')
>>> d
deque(['a', 'b', 'c', 'e'])
>>> d.extend(['f','g','h'])
>>> d
deque(['a', 'b', 'c', 'e', 'f', 'g', 'h'])
>>> d.extendleft(['A','B','C','D'])
>>> d
deque(['D', 'C', 'B', 'A', 'a', 'b', 'c', 'e', 'f', 'g', 'h'])
>>> d[0],d[1],d[-1]
('D', 'C', 'h')
>>> 
======== RESTART: C:/Users/jayadana/Documents/dana's work/chainmap.py ========
>>> c
ChainMap({'a': 0, 'b': 1}, {'b': 2, 'c': 3}, {'d': 4})
>>> c['a'],c['b'],c['c'],c['d']
(0, 1, 3, 4)
>>> c['e'] = 5
>>> c
ChainMap({'a': 0, 'b': 1, 'e': 5}, {'b': 2, 'c': 3}, {'d': 4})
>>> d2
{'b': 2, 'c': 3}
>>> d2['d'] = 6
>>> c
ChainMap({'a': 0, 'b': 1, 'e': 5}, {'b': 2, 'c': 3, 'd': 6}, {'d': 4})
>>> c['f']
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c['f']
  File "C:\Users\jayadana\AppData\Local\Programs\Python\Python37-32\lib\collections\__init__.py", line 914, in __getitem__
    return self.__missing__(key)            # support subclasses that define __missing__
  File "C:\Users\jayadana\AppData\Local\Programs\Python\Python37-32\lib\collections\__init__.py", line 906, in __missing__
    raise KeyError(key)
KeyError: 'f'
>>> c['f']
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c['f']
  File "C:\Users\jayadana\AppData\Local\Programs\Python\Python37-32\lib\collections\__init__.py", line 914, in __getitem__
    return self.__missing__(key)            # support subclasses that define __missing__
  File "C:\Users\jayadana\AppData\Local\Programs\Python\Python37-32\lib\collections\__init__.py", line 906, in __missing__
    raise KeyError(key)
KeyError: 'f'
>>> c['d']
6
>>> c['a'],c['a'],
KeyboardInterrupt
>>> c['a'],c['b'],c['c'],c['d'],c['e']
