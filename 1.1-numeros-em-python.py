# AULA COMPLETA: NUMEROS EM PYTHON

""" 
Vamos aprender:
1- Tipos numéricos
2- Conversões de tipos
3- Hierarquia numérica
4- Operações matemáticas
5- Coerção de tipos 
6- verificação de tipos 
7- Entradas de dados
"""
# PASSO 01 - TIPOS NUMÉRICOS
# int -> Inteiros
# float -> números com casas decimais
# complex -> (usado em mmatemática/engenharia)

print("===== TIPOS NUMÉRICOS =====")

# EXEMPLO 01 - NUMERO INTEIRO

#criamos uma variável chamada numero_inteiro
numero_inteiro = 10

#Mostramos o valor
print ("valor:", numero_inteiro)

print ("Tipo:", type(numero_inteiro))

print("------------------------")

#  EXEMPLO 02 - NUMERO DECIMAL

# Float é um numero com ponto decimal
numero_decimal = 3.14

print ("Valor:", numero_decimal)
print ("Tipo:", type(numero_decimal))



# EXEMPLO 03 - NUMERS COMPLEXOS
# um número complexo possui duas partes:
# Parte real (Numero normal)
# Parte Imaginária (multiplicada por j)

# Estrutura Geral:
# numero = a + bj

# a = parte real
# b = parte imaginária
# j = unidade imaginária

numero_complexo = 2 + 3j

print("Valor:", numero_complexo)
print ("Tipo", type(numero_complexo))

print("-------------------------")

# EXEMPLO 03 ACESSANDO CADA PARTE DO NÚMERO 

# .real retorna a parte real
print ("Parte Real:", numero_complexo.real)
       
#  .imag retorna a parte imaginária
print ("Parte Imaginária:",  numero_complexo.imag)

# apenas pra separar visualmente a saída no terminal
print("\n\n")

#=============================
## PASSO 02 - CONVERSÃO TIPOS
#=============================


## Exemplo Clássico:
## Dados vindos do usuário são texto (string), muitas vezes é necessário converter eles

print ("===== Conversões =====")

# float -> int

valor = int(3.9)

print("int(3.9):", valor)
print("Tipo:", type(valor))

#string -> int
valor1 = "10"
print(type(valor1))

valor2 = int("10")
print('int("10):', valor2)
print("tipo:", type(valor2))


#int --> Float
valor3 = float(10)
print("Tipos:", type(valor3))
