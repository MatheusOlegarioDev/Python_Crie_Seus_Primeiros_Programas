Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Formantando Textos
>>> #Coding: UTF-8
>>> 
>>> "Copa 2022"
'Copa 2022'
>>> 'Copa do Mundo 2014'
'Copa do Mundo 2014'
>>> '''Eu amo Python '''
'Eu amo Python '
>>> "Eu 'Amo Python' "
"Eu 'Amo Python' "
>>> 'Eu Amo "Python"'
'Eu Amo "Python"'
>>> print("""\ Uso: Consulta_Base[OPCOES] """)
\ Uso: Consulta_Base[OPCOES] 
>>> string = "Matheus"
>>> string[0]
'M'
>>> string[1:4]
'ath'
>>> string[2:]
'theus'
>>> string[:3]
'Mat'
>>> len(string)
7
>>> "m" in "string"
False
>>> "M" in "string"
False
>>> "m" not in "string"
True
>>> "M" + "atheus"
'Matheus'
>>> "M" in "Matheus"
True
>>> "M" * 3
'MMM'
>>> minha_str = "livro python 3"
>>> minha_str = minha_str[0:13] + "2"
>>> print(minha_str)
livro python 2
>>> minha_str = minha_str.replace("3", "2")
>>> print(minha_str)
livro python 2
>>> 
>>> #Principais Métodos
>>> 
>>> "Matheus".capitalize()
'Matheus'
>>> "Matheus".count("a")
1
>>> "Matheus".startswith("M")
True
>>> "Matheus".endswith("s")
True
>>> "Eu amo Python".split(" ")
['Eu', 'amo', 'Python']
>>> " ".join(["Eu", "amo", "Python"])
'Eu amo Python'
>>> "Eu amo Python".replace("2020", "2021")
'Eu amo Python'
>>> "Eu amo Python".replace("Python", "Lasanha")
'Eu amo Lasanha'
>>> 
>>> 
>>> #Interpolação de String
>>> 
>>> "%d dias para copa" % (100)
'100 dias para copa'
>>> "{} dias para copa".format(100)
'100 dias para copa'
>>> "{dias} dias para copa".format(dias=100)
'100 dias para copa'
>>> 
>>> 
>>> '{:60}'.format('Alinhado á esquerda, ocupando 60 posições')
'Alinhado á esquerda, ocupando 60 posições                   '
>>> '{:<60}'.format('Alinhado á esquerda, ocupando 60 posições')
'Alinhado á esquerda, ocupando 60 posições                   '
>>> '{:>60}'.format('Alinhado á direita, ocupando 60 posições')
'                    Alinhado á direita, ocupando 60 posições'
>>> '{:^60}'.format('Centralizado, ocupando 60 posições')
'             Centralizado, ocupando 60 posições             '
>>> '{:.^60}'.format('Centralizando ao alterar caractere de espaçamento')
'.....Centralizando ao alterar caractere de espaçamento......'
>>> 
