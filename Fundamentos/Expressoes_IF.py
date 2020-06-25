Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> imposto = 0.3
>>> "Alto!" if imposto > 0.27 else "Baixo!"
'Alto!'
>>> imposto = 0.10
>>> "Alto" if imposto > 0.27 else "Baixo!"
'Baixo!'
>>> 
valor_imposto = "Alto!" if imposto > 0.27 else "Baixo"
>>> valor_imposto
'Baixo'
>>> 
