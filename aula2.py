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


#terceiro operador é o maior que ">" , so serve para numeros, exemplos

op= 10 > 9
print(op)
#nesse caso ele verifica se um numero é maior que o outro e retorna true ou false , nesse caso true

op= 10 > 11
print(op)
#nesse caso ele retornarar false , pois o numero da direita é maior que o da esquerda


#quarto operador é o menor que "<" , so serve para numeros, exemplos

op= 18 < 19
print(op)
#nesse caso ele verifica se um numero é menor que o outro e retorna true ou false , nesse caso true

op= 20 < 19
print(op)
#nesse caso ele retornarar false , pois o numero da direita é menor que o da esquerda


#quinto operador é o maior ou igual  que ">=" , so serve para numeros, exemplos

op= 10 >= 9
print(op)
#nesse caso ele verifica se um numero é maior ou igual que o outro e retorna true ou false , nesse caso true

op= 10 >= 11
print(op)
#nesse caso ele retornarar false , pois o numero da direita é maior ou diferente que o da esquerda

op= 17 >= 17
print(op)
#nesse caso ele retornarar true , pois o numero da direita é igual o da esquerda

#sexto operador é o menor ou igual que "<" , so serve para numeros, exemplos

op= 18 <= 19
print(op)
#nesse caso ele verifica se um numero é menor ou igual que o outro e retorna true ou false , nesse caso true

op= 20 <= 19
print(op)
#nesse caso ele retornarar false , pois o numero da direita é menor ou diferente que o da esquerda

op= 20 <= 20
print(op)
#nesse caso ele retornarar true , pois o numero da direita é igual o da esquerda



#operadores de atribuiçao


#para simplificar algumas operações se usam os operadores de atribuiçao , exemplos:

x= 10  
#definimos uma variavel x com o valor dez

#normalmente para somar algo a esse valor usamos essa forma
#x=x+5
#mas para simplificar usaremos :

#x +=5
#print(x)

#o mesmo vale para as outras operações:
#subtração:
#x=x-5

#x -=5
#print(x)

#multiplicação:
#x=x*5

#x *=5
#print(x)

#divisão:
#x=x/5

#x /=5
#print(x)

#existe uma forma de obtermos o resto da divisao com a porcentagem "%", exemplo

#x=x%3

#onde aqui ele retorna "1" que seria o resto da divisao de x por 3 , no caso 10 por 3, que o resultado seria 3 e resto 1
#simplificando:

x %=3
print(x)

'''
