Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from datetime import date
>>> d = (2013, 3, 15)
>>> date(d[0], d[1], d[2])
datetime.date(2013, 3, 15)
>>> #Packing
>>> from datetime import date
>>> d = (2013, 3, 15)
>>> date(*d)
datetime.date(2013, 3, 15)

