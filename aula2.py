'''
#calculos em python
#em python segue a ordem das operaçoes 
#exponencial = **
#parenteses = (2+2)
#multiplicaçao = *
#divisao = /
#soma e subtraçao = + -
#exemplos:

calculo1= (2+2)**3 * 4 /2 + 3 -1 
print (calculo1)
#nesse exemplo ele primeiro faz o exponencial para partir para as outras operações onde o resultado é 130.

calculo2= (2+2) * 4 /2 + 3 -1 
print (calculo2)
#nesse exemplo ele primeiro faz o parenteses para partir para as outras operações onde o resultado é 10.

calculo3= 2 * 4 /2 + 3 -1 
print (calculo3)
#nesse exemplo ele primeiro faz a multiplicaçao e divisao(na ordem que estiver) para partir para as outras operações onde o resultado é 6.

calculo4= 2 + 3 -1 
print (calculo4)
#nesse exemplo ele primeiro faz a soma e subtração em ordem que estiver  onde o resultado é 4.


#operadores de comparaçao 
#primeiro operador é o de igualdade "==",alem de numeros , ele tambem serve parar caracteres, segue os exemplos:

op= 10==10
print(op)
#aqui ele verifica se os valores sao iguais e retorna verdadeiro ou falso , nesse caso true.

op= 10==11
print(op)
#aqui ele retorna falso.

op= 'banana'=='banana'
print(op)
#aqui ele verifica cada caracter e julga para ver se é exatamente igual, nesse caso true

op= 'banana'=='banane'
print(op)
#nesse caso apresenta um caracter diferente , logo ele retorna false
#vale lembrar que ele difere de letra maiscula com letra minuscula

#segundo operador é o diferente de "!=",alem de numeros , ele tambem serve parar caracteres, segue os exemplos:

op= 10!=11
print(op)
#aqui ele verifica se os valores sao diferentes e retorna verdadeiro ou falso , nesse caso true.

op= 10!=10
print(op)
#aqui ele retorna falso.

op= 'banana'!='banana'
print(op)
#aqui ele verifica cada caracter e julga para ver se é diferente, como é exatamente igual ,logo nesse caso e false

op= 'banana'!='banane'
print(op)
#nesse caso apresenta um caracter diferente , logo ele retorna true
#vale lembrar que ele difere de letra maiscula com letra minuscula



'''



