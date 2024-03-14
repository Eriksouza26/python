'''
#Funções 
#basicamente usamos a funçoes para amarzenar uma habilidade especifica e chamamos ela em qualquer 
#lugar do codigo sem preecisar reescreve la
#exemplo:

def lingua_solta():
    print('vc deu com a lingua nos dentes ne ?')
#desse forma ai ela nao rertonara nada , é preciso chamar a funçao

lingua_solta()
#assim que se chama a função, simples e facil.


#existe uma diferença de tratamento de variaveis dentro de uma função
#a variavel criada dentro da funçao so existe la mesmo
#logo se tiver uma variavel com mesmo nome do lado de fora
#nao apresentara erro, siga nessa função de somar


def somar():
    soma1=10
    soma2=5
    resultado=soma1+soma2
    print(resultado)


somar()    

soma1=22
print(soma1)
#aqui vemos que ao definir uma variavel de nome igual nao 
# apresenta erro , alem do valor ser diferente

#usando parametros e Argumento podemos dar valores as variaveis dentro da funçao
#exemplo:
#vamos supor que vendemos laptops e precisamos falar para cliente um boa vindas e a 
#quantidade de laptops disponiveis:


def boas_vindas(nome,qntd):#dentro do parenteses colocamos nossos parametros que receberao os valores
    print(f'Ola {nome}, seja bem vindo')
    print(f'Temos {str(qntd)} laptops disponiveis.') 


boas_vindas('Ricardo',5)#aqui definimos os valores , chamados de argumentos , detalhe str sempre entre ''
boas_vindas('Giseli',3)
boas_vindas('Fin',1)

#podemos ja predefenir o valor de um parametro se liga:
def boas_vindas(nome,qntd=10):#preste atençao! o parametro que voce ja definir aqui deve ser sempre os ultimos , tem ordem
    print(f'Ola {nome}, seja bem vindo')
    print(f'Temos {str(qntd)} laptops disponiveis.') 


boas_vindas('Giseli')#aqui vemos que se voce nao passar o argumento , nao tera problemas.
boas_vindas('Fin',3) # e aqui vemos que se mesmo assim voce passar ele so ira mudar la.


#podemos dizer que as funçoes podem armazenar um valor ,ser liga:

def cliente1(nome):
    print(f'ola {nome}')#essa é uma funçao vazia , nao armazena valor nenhum logo se colocarmos ela em um print:


#print(cliente1('maria'))
#ela retornara none ,indicando que nao tem valor armazenado

def cliente2(nome):
    return f'ola {nome}'#usando o return ele armazena o valor


#print(cliente2('Jose'))#aqui percebemos que ele retorna o valor definido

#se adicionarmos a uma variavel:

x=cliente1('Maria')
y=cliente2('Jose')

print(x)#aqui sera a mesma coisa , sem valor
print(y)#aqui mostrara o valor armazenado

#Em resumo em função , use print para quais tarefas nao precisem
# armazenar um valor que vai usar depois, ela so mostrara  na tela e use o return caso
# precise que a funçao armazene um valor para usar posteriormente.Lembrando que o return nao imprime nada


#Varios argumentos(xargs)
#podemos passar varios argumentos para um so parametro... vamos usar um exemplo
#quero somar todos os numeros que passar de argumentos e printar o resultado

def somar(*numeros): #ao usar * ele indentifica que serao varios argumentos em um parametro de variavel
    resultado=0 #precisamos zerar o resultado para que o for possa ter um ponto de partida
    for num in numeros: #aqui o num armazena um  valor de cada vez do numeros 
        resultado += num #aqui se adiciona o num ao valor anterior 
    return resultado    #aqui é armazenado na funçao o valor .


x=somar(2,3,5,7)#sao passados varios argumentos como visto, 
# coloquei a funçao em uma variavel para adicionar o valor dela na variavel 
print(x)



#vimos que podemos usar varios argumentos , mas podemos usar tambem varios parametros 
#para exemplo , somos uma concessionaria onde precisamos especificar cada  coisa da tabela



def carros(**lista): #basta adicionar mais um * para indicar varios parametros
    return lista
    

print(carros(Marca='Wolks',Cor='Branca',Motor= 1.0))
print(carros(Marca='Ford',Cor='Preto',Motor= 1.6, Placa='QPP9A34' ))
print(carros(Marca='Fiat',Cor='Vermelho'))

#podemos usar codigos ja escritos e poupar um certo tempo, esses sao chamados MODULOS    
#como exemplo que tal uma questao de matematica? preciso do fatorial dos numeros
#de numeros pequenos seria simples:
#fatorial do numero 4
fatorial=1*2*3*4
print(fatorial)
#certo assim é bem simples , mas e se o numero for 56? ficaria complicado fazer manualmente
#para isso usaremos um Modulo 

import math #math é um modulo voltado para matematica

x=math.factorial(56) #aqui chamamos uma "funçao" do modulo math e armazenamos o resultado numa variavel
print(x)
#math tem varios outras funçoes , o uso de modulos é simples , para achal-los é preciso pesquisar um pouco

print(math.sqrt(2)) #esse é para a raiz quadrada

print(math.floor(2.6)) #esse joga para a casa decimal mais baixa

print(math.ceil(2.6)) #esse joga para a casa decimal mais alta

print(math.pow(2,1)) #esse é a elevaçao primeiro parametro é o que vai ser elevado e o segundo a elevaçao,retorna em float
'''

