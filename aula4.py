'''
#While loop
#agora utilizaremos o while para fazermos um loop , ele é otimo parea loopings que dependem de condiçoes.
#no seguinte temos um problema demonstrar o uso do while. Preciso vender um produto onde a cada dia ele
#entra numa promoção que reduz o valor dele em R$5,00 , mas nao posso vender por menos de 20 para ter lucro

valor=100
dia=0

while valor>20:
    dia+=1
    print(f'no dia {dia} o produto tera o valor de R${valor}')
    valor-=5
    
    
#para o proximo exemplo vamo ser um revendedor onde se o produtor for mais que R$20 adicionamos 
#10% em cima do valor 


valor=int(input('Digite o valor do seu produto:'))

while valor>20:
    valor=(valor*0.1)+valor
    print(f'O valor do profuto sera R${valor}')
    
    break #usamos o break para nao rodar infinitamente

    
'''


