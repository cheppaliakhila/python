Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="aadvvhadfsdfh"
>>> print(s.count('a'))
3
>>> print(s.count('vv'))
1
>>> print(s.count('d',2,8))
2
>>> print(s.count('d',2,12))
3
