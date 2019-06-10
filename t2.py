Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> square
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
========== RESTART: C:/Users/jayadana/Documents/dana's work/comb.py ==========
>>> (x,y)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    (x,y)
NameError: name 'x' is not defined
>>> 
========== RESTART: C:/Users/jayadana/Documents/dana's work/comb.py ==========
>>> (x,y)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    (x,y)
NameError: name 'x' is not defined
>>> 
========== RESTART: C:/Users/jayadana/Documents/dana's work/comb.py ==========
Traceback (most recent call last):
  File "C:/Users/jayadana/Documents/dana's work/comb.py", line 1, in <module>
    (x,y) = [(x,y) for x in [3,1,2] for y in [2,1,3] if x != y]
ValueError: too many values to unpack (expected 2)
>>> 
========== RESTART: C:/Users/jayadana/Documents/dana's work/comb.py ==========
>>> n
[(3, 2), (3, 1), (1, 2), (1, 3), (2, 1), (2, 3)]
>>> 
========== RESTART: C:/Users/jayadana/Documents/dana's work/comb.py ==========
>>> vec
[-4, -3, -2, 1, 2, 3]
>>> 
========== RESTART: C:/Users/jayadana/Documents/dana's work/comb.py ==========
>>> x
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> 
========== RESTART: C:/Users/jayadana/Documents/dana's work/comb.py ==========
>>> m
[1, 2, 3]
>>> 
========== RESTART: C:/Users/jayadana/Documents/dana's work/comb.py ==========
>>> n
[4, 3, 2, 1, 2, 3]
>>> 
========== RESTART: C:/Users/jayadana/Documents/dana's work/comb.py ==========
>>> c
[(0, 0), (1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]
>>> 
========== RESTART: C:/Users/jayadana/Documents/dana's work/comb.py ==========
>>> f
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> r
['3.0', '3.1', '3.14', '3.142', '3.1416', '3.14159']
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> r
[3, 3, 3, 3, 3, 3]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> r
[3.0, 3.1, 3.14, 3.142, 3.1416, 3.14159]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> mr
[[1, 5, 9], [2, 6, 10], [3, 7, 11]]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> mc
[[1, 5, 9], [2, 6, 10], [3, 7, 11]]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
Traceback (most recent call last):
  File "C:/Users/jayadana/Documents/dana's work/sq.py", line 18, in <module>
    prime = [[a,b] for x in range(2,n) if n%x ==0]
NameError: name 'n' is not defined
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
Traceback (most recent call last):
  File "C:/Users/jayadana/Documents/dana's work/sq.py", line 18, in <module>
    prime = [[] for x in range(2,n) if n%x ==0]
NameError: name 'n' is not defined
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
Traceback (most recent call last):
  File "C:/Users/jayadana/Documents/dana's work/sq.py", line 19, in <module>
    prime = [tableaux[0,0] for i in range(2,n) if n%x ==0]
NameError: name 'n' is not defined
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
Traceback (most recent call last):
  File "C:/Users/jayadana/Documents/dana's work/sq.py", line 19, in <module>
    prime = [tableaux[0,0] for i in range(2,10) if n%x ==0]
  File "C:/Users/jayadana/Documents/dana's work/sq.py", line 19, in <listcomp>
    prime = [tableaux[0,0] for i in range(2,10) if n%x ==0]
NameError: name 'n' is not defined
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
Traceback (most recent call last):
  File "C:/Users/jayadana/Documents/dana's work/sq.py", line 19, in <module>
    prime = [tableaux[0,0] for i in range(2,10) if i%2 ==0]
  File "C:/Users/jayadana/Documents/dana's work/sq.py", line 19, in <listcomp>
    prime = [tableaux[0,0] for i in range(2,10) if i%2 ==0]
NameError: name 'tableaux' is not defined
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> prime
[[0, 0], [0, 0], [0, 0], [0, 0]]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> prime
[[0, 2], [0, 2], [0, 2], [0, 2], [0, 2]]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> prime
[[2], [2], [2], [2], [2]]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> prime
[[], [], [], [], []]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> prime
[0, 0, 0, 0, 0]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
>>> prime
[19, 19, 19, 19, 19]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
3 is a prime number
4 equals 2 * 2
5 is a prime number
5 is a prime number
5 is a prime number
6 equals 2 * 3
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 equals 2 * 4
9 is a prime number
9 equals 3 * 3
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
3 is a prime number
4 equals 2 * 2
5 is a prime number
5 is a prime number
5 is a prime number
6 equals 2 * 3
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 equals 2 * 4
9 is a prime number
9 equals 3 * 3
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
3 is a prime number
4 equals 2 * 2
5 is a prime number
5 is a prime number
5 is a prime number
6 equals 2 * 3
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 equals 2 * 4
9 is a prime number
9 equals 3 * 3
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
3 is a prime number
4 equals 2 * 2
5 is a prime number
5 is a prime number
5 is a prime number
6 equals 2 * 3
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 equals 2 * 4
9 is a prime number
9 equals 3 * 3
>>> l
[(4, 2), (6, 2), (6, 3), (8, 2), (8, 4), (9, 3)]
>>> 
=========== RESTART: C:/Users/jayadana/Documents/dana's work/sq.py ===========
3 is a prime number
4 equals 2 * 2
5 is a prime number
5 is a prime number
5 is a prime number
6 equals 2 * 3
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 equals 2 * 4
9 is a prime number
9 equals 3 * 3
10 equals 2 * 5
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
12 equals 2 * 6
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
14 equals 2 * 7
15 is a prime number
15 equals 3 * 5
16 equals 2 * 8
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
18 equals 2 * 9
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
>>> 
