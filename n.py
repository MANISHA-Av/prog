Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import namedtuple
>>> a=namedtuple('course', "name, technology")
>>> s=a("data science", "python")
>>> print(s)
course(name='data science', technology='python')
>>> from collections import namedtuplea=namedtuple('course', "name, technology")
SyntaxError: invalid syntax
>>> from collections import namedtuple
>>> a=namedtuple('course', "name, technology")
>>> s=a._make("data science", "python")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s=a._make("data science", "python")
TypeError: _make() takes 2 positional arguments but 3 were given
>>> from collections import namedtuple
>>> a=namedtuple('course', "name, technology")
>>> s=a._make(["data science", "python"])
>>> print(s)
course(name='data science', technology='python')
>>> from collections import deque
>>> a=["a","b","c","d","e","f"]
>>> s=deque(a)
>>> print(s)
deque(['a', 'b', 'c', 'd', 'e', 'f'])
>>> s.append("python")
>>> print(s)
deque(['a', 'b', 'c', 'd', 'e', 'f', 'python'])
>>> s.pop()
'python'
>>> print(s)
deque(['a', 'b', 'c', 'd', 'e', 'f'])
>>> s.popleft()
'a'
>>> print
<built-in function print>
>>> print(s)
deque(['b', 'c', 'd', 'e', 'f'])
>>> 
>>> 
>>> 
>>> 
>>> from collections import chainMap
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    from collections import chainMap
ImportError: cannot import name 'chainMap' from 'collections' (C:\Users\manisha\AppData\Local\Programs\Python\Python38-32\lib\collections\__init__.py)
>>> from collections import ChainMap
>>> a={1:"manisha", 2:"anshika"}
>>> b={3:"asdf", 4:"dkmkm"}
>>> c=ChainMap(a,b)
>>> print(c)
ChainMap({1: 'manisha', 2: 'anshika'}, {3: 'asdf', 4: 'dkmkm'})
>>> 