# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

#No gabarito o professor usou funções
#Tentei fazer utilizando somente a condicional, mas não funcionou. 
#Tentei fazer no jupyter e funcionou, dai tentei aqui e foi. 

print("\n******************* Python Calculator *******************")

#Mensagem /contexto
print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

#Receber info /operação
ope = int(input("\nDigite sua opção (1/2/3/4): "))

#Receber info /valores
x = int(input("\nDigite o primeiro número: "))
y = int(input("\nDigite o segundo número: "))

#Condicional /usando a operação escolhida
if ope == 1:
    #Calculo da adição
    print("Resultado: ")
    a = x+y
    print(x," + ",y," = ",a)
elif ope == 2:
    #Calculo da subtração
    print("Resultado: ")
    b = x-y
    print(x," - ",y," = ",b)
elif ope == 3:
    #Calculo da multiplicação
    print("Resultado: ")
    c = x*y
    print(x," * ",y," = ",c)
elif ope == 4:
    #Calculo da divisão
    print("Resultado: ")
    d = x/y
    print(x," / ",y," = ",d)
else:
    #Caso escolha uma opção não existente
    print("\n")
    print("\nOpção Inválida!")