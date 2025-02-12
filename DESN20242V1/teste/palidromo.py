def eh_palindromo(palavra):
    # Remover espaços e converter para minúsculas para garantir a comparação correta
    palavra = palavra.replace(" ", "").lower()
    # Verificar se a palavra é igual à sua reversa
    return palavra == palavra[::-1]

# Testando a função
palavra = input("Digite uma palavra ou frase: ")
if eh_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo!')
