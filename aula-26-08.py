'''  Scripts criados na aula sobre variáveis, operadores aritméticos, variáveis dinâmica, listas '''

# divisão da parte inteira
x = 30 // 12
print(x)

# módulo
x = 10 % 5
print(x)

# tipo da variável
var1 = "oi"
var2 = 20
var3 = 10/9
var4 = True

print('')
print( type(var1))
print( type(var2))
print( type(var3))
print( type(var4))

# se concateca float com , se quiser usar o + tem q converter para String
nota = 10 * (0.3+0.07*0.80)
print('\nNota do quizizz', nota)

# contando os caracteres de uma String
frase = 'oi, boa noite'
print('A frase "oi, boa noite" tem : ',len(frase), ' caracteres')
print('')

# inicializacao | parada | 
# [3::3] -> pular de 3 em 3 caracteres ate o final da string
frase = 'fajsfjiawj9323rm@34afe'
print(frase[3::3])
print('')

# manipulação de string
# nao se pode modificar, somente incrementar com uma manipulação externa (criando nova variável)
txt1 = 'Julia'
txt2 = txt1[:-1] + 'o'
print(txt2)
print('')

# inteiro * string 
# repetindo palavras
palavra = 'oi '
repeticao = 3*palavra
print(repeticao)
print('')

# separar as palavras por espaços em branco, criando um objeto começando da posição [0]
frase = 'Quantas palavras será que tem nessa frase ?'
print(frase.split())
# contando numero de caracteres
print(len(frase.split()))
# engolindo as letras A e divide a palavra onde é "cortada"
print(frase.split('a'))
# saber quantas letras tem em um texto
print(len(frase.split('a'))-1)
print('')

# imprimir uma sequencia de informações em ordem especifica
carros = 'Meus carros são: {0}, {2}, {0}, {4}, {0}'
carro0 = 'ka'
carro1 = 'gol'
carro2 = 'argo'
carro3 = 'bravo'
carro4 = 'virtus'
print( carros.format(carro0, carro1, carro2, carro3, carro4 ) )
print('')

# listas!
lista1 = [4, 'IESB', 11.4, False]
print(lista1)
print(len(lista1))


# Saída 

''' 
2
0

<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>

Nota do quizizz 3.5599999999999996
A frase "oi, boa noite" tem :  13  caracteres

sij2m4e

Julio

oi oi oi

['Quantas', 'palavras', 'será', 'que', 'tem', 'nessa', 'frase', '?']
8
['Qu', 'nt', 's p', 'l', 'vr', 's será que tem ness', ' fr', 'se ?']
7

Meus carros são: ka, argo, ka, virtus, ka

[4, 'IESB', 11.4, False]
4
'''
