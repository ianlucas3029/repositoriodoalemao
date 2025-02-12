n = int(input("Digite um numero inteiro positivos: "))
numero = 2
divisores = 0 # divisores é a variavel contadora

while (numero <= n-1):
    if  (n % numero == 0) : #se ele é divisivel por numero
        divisores = divisores + 1
    numero = numero + 1

if (divisores == 0):
    print ("é primo.")
elif (divisores == 1):
    print(" =Não é primo. possui 1 divisor diferente de 1 e" ,n)
else :
    print("nao é primo. possui", divisores, "divisores diferentes de 1 e" ,n)