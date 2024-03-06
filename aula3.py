'''
#Condicionais 
#para verificarmos se em uma condição é valida usamos if , else e elif, a seguir 
#teremos um problema para ilustramos e explicar essas condiçoes.
#A situação , temos uma via onde a velocidade maxima permitida é 110km/h,
#verificaremos se o condutor esta na velocidade , acima ou muito abaixo:

#velocidade=100

#declaramos a velocidade do condutor
velocidade= input('qual a velocidade do condutor ')
#aqui usaremos o input para que o usuario possa interagir com nós.Ele nos informara a velociade do condutor
velocidade= int(velocidade)
#aqui transformamos a informação que recebemos em inteiro, pois sempre que usamos o inpu eles nos volta como string

if velocidade > 110 :
    print('Velocidade maxima da via ultrapassada')
    #aqui verificamos se a velocidade do condutor é maior que a da via 
    #se for, retornara a mensagem acima 
elif velocidade < 60:
    print('Para sua segurança dirija acima de 60km/h')
    #aqui caso o condutor nao ultrapasse o limite da via , mas
    #esteja numa velocidade muito baixa , ele retornara essa mensagem
else:
    print('velocidade ok')
    #caso nao ocorra nenhuma das outras situaçoes, caira nessa, onde 
    #ela retorna a mensagem acima.          




#Operadores logicos
#os operadores logicos servem para mais de uma condiçao
#usamos 'and' para quando é necessario que todas as sentenças sejam verdadeiras 
#e 'or' para que pelo menos uma das sentenças seja verdadeira 
#Usaremos como exemplo o sistema de banco, onde é necessario ter uma renda e ter o nome limpo:

nomelimpo= True
rendaacimade3mil=True
#para essa questao usaremos variaveis bolianas "True/False"

if nomelimpo and rendaacimade3mil:
    print('Aprovado')
else:
    print('Negado')


#nessa operaçao usamos o 'and' para veficar as veracidade de ambas informações , nesse caso ambas
#sao verdadeiras , logo sera aprovado 
#mas se trocarmos uma das variaveis por 'False'...

nomelimpo= True
rendaacimade3mil=False

if nomelimpo and rendaacimade3mil:
    print('Aprovado')
else:
    print('Negado')


#Podemos ver que sera negado , pois a condição de 'and' é que todas as sentenças sejam verdadeiras 
#agora usaremos o 'or':         


nomelimpo= True
rendaacimade3mil=True

if nomelimpo or rendaacimade3mil:
    print('Aprovado')
else:
    print('Negado')

#Nessa situação se todos forem verdade , sera aprovado


nomelimpo= False
rendaacimade3mil=True

if nomelimpo or rendaacimade3mil:
    print('Aprovado')
else:
    print('Negado')
    
#Tambem sera aprovado se so um dos dois for verdadeiro
     
nomelimpo= False
rendaacimade3mil=False

if nomelimpo or rendaacimade3mil:
    print('Aprovado')
else:
    print('Negado')
     
#Mas se todos forem falso sera negado  



#Looping
#para fazermos uma tarefa repitida vezes usaremos o 'for', onde ele mesmo fara o trabalho de repetir
#vamos usar de exemplo um jeito de fazer uma lista de 1 a 100

#for numero in range(100):
 #   print(numero)
    
#para explicar aqui usamos o 'for' depois damos uma variavel para ele , nesse caso 
#é a variavel numero logo depois falamos 'in range' e o numero de vezes que queremos repetir
#Mas nessa forma ele ira de 0 a 99 e nao de 1 a 100, pois ele conta como index que começa do 0
#podemos alterar isso
 
#for numero in range(1, 101):
 #   print(numero)

#Dessa forma ele nao contara o zero , mas é preciso adicionar mais um para que chegue ate a 100
#mas podemos usar o "range"  para outras coisas, usamos como parametro (começo, fim ,incremento):

#for numero in range(1, 101 ,2):
 #   print(numero)

#dessa forma ele pulara de 2 em 2 numeros , logo assim trazendo somente numeros impares
#para trazer os pares:

#for numero in range(0, 101 ,2):
 #   print(numero)

#tambem podemos usar o for para percorrer strings , usando index , como exemplo:
#vamos percorrer a palavra google e nos retorna cada caracter em cada linha separada 

palavra='Google'

#para facilitar vamos adicionar a uma variavel

#for letra in palavra:
   # print(f'{letra}')
           #utilizamos a formataçao para ficar mais bonitinho e facilitar posteriormente

#vamos melhorar:
for letra in palavra:
    print(f'{letra} esta presente na palavra {palavra}')

# e se tentarmos com uma frase maior ?    

pala='Ola mundo'

for letra in pala:
    print(f'{letra}')
    
# da muito certo!!
   
   
#Looping com condiçao

#agora usaremos as condiçoes dentro de um loop, para exemplo usaremos uma loja
#onde é preciso enviar um email com detalhes da compra para um usuario 
#mas tem as seguintes condições : O pagamento precisa estar feito e tem no maximo 3 tentativas para envio do email


compraconfirmada=True #dessa forma o loop vai parar na primeira tentativa , mas se for False ele rodara as 3 vezes.
email='entrega confirmada'

for tentativa in range(3):
    if compraconfirmada:
        print('compra confirmada')
        print(f'A seguinte mensagem foi enviada para o seu email: {email} ')
        break #se coloca o 'break' para caso a compra for confirmada na primeira tentativa ele ja saia do loop
else:
    print('Falha na compra')
        

#Vamos supor que um jornal quer que imprima um espaço entre todas as palavras , como fazer?


palavra='FANTASTICO MUNDO DE GAMBALL'
#vamos criar a variavel com o texto

for space in palavra:#vamos percorrer a string
    print(f' {space}', end='')#pronto  aqui imprimimos de maneira formatada inserindo um espaço antes da string
    #e usamos o 'end' para dizer ao print para nao pular a linha se houver um ''.

   

#Vamos criar um retangulo de simbolos  com o for

linhas=6
colunas=6
simbolo='@'

#definimos o numero de linhas e colunas e o simbolo que vamos utilizar


for l  in range(linhas):
    for c in range(colunas):
        print(f'{simbolo}',end='')
    print()    
#para explicar o que foi feito , colocamos um for dentro de outro
#chamaremos um for de linha e o outro de colunas ,a cada 1 vez que o for linha roda
# o for colunas roda 6 vezes , para que haja a quebra de linha inserimos um
#"print()" vazio no final de for linha , assim cada vez q ele rodar o for colunas
# ele vai fazer uma quebra de linha.   

   
   
'''



           
           