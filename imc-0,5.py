import os
os.system("cls")


peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc < 25:
    print("Você está no peso adequado")
elif imc < 30:
    print("Você está com sobrepeso")
else:
    print("Você está com obesidade")
