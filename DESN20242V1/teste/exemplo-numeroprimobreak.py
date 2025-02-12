n = int(input("Digite um número inteiro positivo: "))

numero = 2
primo = True # primo é a variavel indicadora

while (numero <= n-1) and (primo):
    if(n % numero == 0): # se n é  divisivel por numero
        primo = False
    numero = numero + 1
if (primo):
        print("É primo.")
else:
     print(" Não é primo.")