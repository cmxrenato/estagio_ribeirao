
entrada = input("Digite uma palavra: ")
contador = 0
for letra in entrada:
    if letra == "a" or letra == "A":
        contador += 1

print(f"O número de letras 'A' na palavra {entrada} é: {contador}")
