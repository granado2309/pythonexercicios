#n = int(input('Dígite um número '))

#n1 = n * 1
#n2 = n * 2
#n3 = n * 3
#n4 = n * 4
#n5 = n * 5
#n6 = n * 6
#n7 = n * 7
#n8 = n * 8
#n9 = n * 9
#n10 = n * 10
#print('A tabuada de {} é' .format (n),(n1),(n2),(n3),(n4),(n5),(n6),(n7),(n8),(n9),(n10))

#n = int(input('Ecreva um número para ver a sua tabuada:'))
#t = n*1,n*2,n*3,n*4,n*5,n*6,n*7,n*8,n*9,n*10
#print(f'A tabuada do número {n} do 1 ao 10 respectivamente é: {t}')


from os import system ,startfile
from time import sleep

            opcao =1
            while opcao != 0:
                   print('')
                   print('Exercícios')
                   print('')
                   print('9) Tabuada')
                   opcao = int(input('Dígite a opção desajada, ou zero para sair:'))

                   if opcao==9:
                                      #Exercício tabuada

                        num = int(input('Digite um número para ver sua tabuada: '))
                        print('-'* 12)
                        print('{} x {:2} = {}' .format(num,1,num*1))
                        print('{} x {:2} = {}' .format(num,2, num*2))
                        print('{} x {:2} = {}' .format(num, 3,num*3))
                        print('{} x {:2} = {}' .format(num, 4,num*4))
                        print('{} x {:2} = {}' .format(num, 5,num*5))
                        print('{} x {:2} = {}' .format(num, 6,num*6))
                        print('{} x {:2} = {}' .format(num, 7,num*7))
                        print('{} x {:2} = {}' .format(num, 8,num*8))
                        print('{} x {:2} = {}' .format(num, 9,num*9))
                        print('{} x {:2} = {}' .format(num, 10,num*10))
                        print('-'*12)












