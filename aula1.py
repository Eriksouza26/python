'''
aula 1
exemplo 1:
fruta= 'abacate'
#index  0123456
#o index sao os valores representado para cada caracter 

print(fruta[3])
#puxa somente um caracter da palavra , onde os valores são a=0 b=1 a=2 c=3 a=4 t=5 e=5
print(fruta[2:6])
#puxa do valor 2 ao 6.
print(fruta[-1])
#valores negativos puxam de tras para frente , onde os valores são -1=e -2=t -3=a -4=c -5=a -6=b -7=a

exemplo 2:
valor= 99.75
#index 01234
#para puxarmos somente os centavos.
print(valor[3:5])
#esse modo so funciona para strings , logo é preciso converter para str
valor=str(valor)
print(valor[3:5])
'''
'''string formatada 
#primeiro exemplo : O erik souza e um excelente [programador]
 
nome= 'erik '
sobrenome= 'souza ' 
profissao= 'programador'

texto= 'O ' + nome + sobrenome + 'e um excelente ' + '[' +profissao + ']'
#jeito mais complicado de formataçao
print(texto)

texto2=f'O {nome} {sobrenome} e um excelente [{profissao}]'
#jeito mais facil de formataçao, colocando um "f".
print(texto2)
 '''

'''metodos dentro de uma string
mensagem='Eu adoro comida caseira'
#index    0123456789...

print(mensagem)
#jeito normal

print(mensagem.lower())
#imprime tudo em letra minuscula

print(mensagem.upper())
#imprime tudo em letra maiscula

print(mensagem.capitalize())
#transforma a primeira letra em maisculo

print(mensagem.find('c'))
#procura a posiçao da letra , lembrando que mostra o index,
#vale lembrar tambem que se colocar em maiusculo vai procurar 
# a letra em maiusculo , se nao houver apresenta -1 como se nao houvesse
# Tambem é possivel ver onde começa a palvra por exemplo :
# print(mensagem.find('adoro')) onde ele retorna 3 indicando o inicio no index 3=a

print(mensagem.replace('a','e'))
print(mensagem.replace('caseira','feita em casa'))
#serve para procurar e substituir o caracter ou palavras

print(mensagem.strip())
#serve para retirar todos os espaços antes do primeiro caracter

'''





