import os
os.system("cls")

print("===== Bem vindo a sua calculadora de IMC =====")

nome = input("digite seu nome: ")
peso = float(input("digite seu peso em KG: "))
altura = float(input("digite sua altura em metros: "))

imc = peso / (altura ** 2)

os.system("cls")

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc < 25:
    print("Você está no peso adequado")
elif imc < 30:
    print("Você está com sobrepeso")
else:
    print("Você está com obesidade")

input("pressione enter para encerrar o programa ")