"""
Em Python, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas. 
A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente. 
Além disso, podemos criar nossos próprios módulos para organizar e modularizar nosso código.
"""
 
"""
SOA_LID_Ten en cuenta-1.png	
Tenha em mente
Python vem com uma ampla biblioteca padrão de módulos que fornecem funcionalidades adicionais. 
Esses módulos estão disponíveis sem a necessidade de instalá-los separadamente.
"""

#Importar módulos

"""
Para utilizar um módulo em nosso programa, devemos importá-lo utilizando a declaração import. 
Podemos importar um módulo completo ou funções específicas de um módulo.
"""

import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

"""
Neste exemplo, importa-se o módulo math utilizando a declaração import. Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz quadrada de 25.
Também podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função.
"""

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0

"""
Neste caso, importa-se apenas a função sqrt() do módulo math, o que nos permite utilizá-la diretamente sem ter que precedê-la com o nome do módulo.
"""

#Funções e classes de módulos padrão

"""
A biblioteca padrão de Python oferece uma ampla gama de módulos com funções e classes úteis. Alguns exemplos comuns incluem:
"""
#MATH

"""
Fornece funções matemáticas, como sqrt() (raiz quadrada), sin() (seno), cos() (cosseno), entre outras.
"""

#RANDOM

"""
Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.
"""

#DATATIME

"""
Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.
"""

import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatório)  # Imprime um número inteiro aleatório entre 1 e 10


data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual

"""
Estes são apenas alguns exemplos dos muitos módulos disponíveis na biblioteca padrão de Python. 
Você pode consultar a documentação oficial de Python para obter mais informações sobre os módulos e suas funcionalidades.
"""

"""
Além de utilizar os módulos padrão do Python, também podemos criar nossos próprios módulos para organizar e reutilizar nosso código.
"""
 
"""
Criar e utilizar módulos personalizados
Para criar um módulo personalizado, simplesmente criamos um novo arquivo Python com o nome desejado e definimos as funções, classes e variáveis que queremos incluir no módulo. 
Por exemplo, criamos um arquivo (no mesmo diretório onde estamos executando Python) chamado meu_modulo.py com o seguinte conteúdo:
"""

#meu_modulo.py
def saudar(nome):
    print(f"Olá, {nome}!")


def calcular_soma(a, b):
    return a + b
Depois, podemos importar e utilizar as funções definidas em meu_modulo.py em outro arquivo Python.

import meu_modulo


meu_modulo.saudar("João")  # Imprime "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  # Imprime 8

"""
Neste exemplo, importa-se o módulo meu_modulo e utilizam-se as funções saudar() e calcular_soma() definidas nele.
"""

"""
Organização do código em módulos
À medida que nossos programas crescem em tamanho e complexidade, é uma boa prática organizar nosso código em módulos separados segundo sua funcionalidade. 
Isso nos permite manter um código mais legível, agrupado em módulos e fácil de manter.
Por exemplo, podemos ter um módulo operacoes.py que contenha funções relacionadas com operações matemáticas, e outro módulo utilidades.py que contenha funções de uso geral.
"""

# operacoes.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

# utilidades.py
def imprimir_mensagem(mensagem):
    print(mensagem)

def obter_nome_usuario():
    return input("Digite seu nome: ")
Depois, podemos importar e utilizar essas funções em nosso programa principal.

import operacoes
import utilidades

resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")

"""
Ao organizar nosso código em módulos, podemos reutilizar funções e manter um código mais estruturado e agrupado em módulos.
"""

"""
Um pacote é uma forma de organizar módulos relacionados em uma estrutura hierárquica de diretórios. 
Os pacotes nos permitem agrupar módulos relacionados e evitar conflitos de nomes entre módulos.
"""
 
"""
Criar e utilizar pacotes
Para criar um pacote, criamos um diretório com o nome desejado e adicionamos um arquivo especial chamado __init__.py dentro do diretório. Este arquivo pode estar vazio ou conter código de inicialização do pacote.
"""

#Por exemplo, criamos um diretório chamado meu_pacote com a seguinte estrutura:

meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py


#Depois, podemos importar e utilizar os módulos do pacote em nosso programa.


from meu_pacote import modulo1, modulo2

modulo1.funcao1()
modulo2.funcao2()

"""
Neste exemplo, são importados os módulos modulo1 e modulo2 do pacote meu_pacote e são utilizadas as funções definidas neles.
"""
#ATENÇÃO!

"""
A importação e criação de módulos e pacotes em Python nos permite organizar e reutilizar nosso código de maneira eficiente. 
Ao modularizar nosso código, podemos manter um código mais legível, estruturado e fácil de manter.
Lembre-se de explorar a biblioteca padrão de Python e aproveitar os módulos existentes, que podem facilitar muitas tarefas comuns. 
Além disso, não hesite em criar seus próprios módulos e pacotes para organizar e reutilizar seu código de maneira eficaz.
"""

