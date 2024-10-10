#conversor de temperatura

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32)* 5/9 + 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


print("escolha a conversão:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
print("3. celsius para kelvin")
print("4. kelvin para celsius")
print("5. fahrenheit para Kelvin")
print("6. kelvin para fahrenheit")

opcao = input("digite a opção: ")

if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius)}°F")
elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"{fahrenheit}°F é igual a {fahrenheit_para_celsius(fahrenheit)}°C")
elif opcao == "3":
    celsius = float(input("Digite a temperatura em Celsius: "))
    print(f"{celsius}°C é igual a {celsius_para_kelvin(celsius)}°K")
elif opcao == "4":
    kelvin = float(input("Digite a temperatura em Kelvin: "))
    print(f"{kelvin}°K é igual a {kelvin_para_celsius(kelvin)}°C")
elif opcao == "5":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"{fahrenheit}°F é igual a {fahrenheit_para_kelvin(fahrenheit)}°K")
elif opcao == "6":
    kelvin = float(input("Digite a temperatura em Kelvin: "))
    print(f"{kelvin}°K é igual a {kelvin_para_fahrenheit(kelvin)}°F")

else:
    print("Opção inválida. Tente novamente.")


