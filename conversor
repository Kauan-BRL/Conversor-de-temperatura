from textwrap import dedent
from sys import exit

def menu_inicial():
    print(f'\n{20*'='} CONVERSOR {20*'='}')
    conversor = f'''\
    {15*'='} TEMPERATURA INICIAL {15*'='}
    [1] Celsius (C)
    [2] Fahreinheit (f)
    [3] Kelvin (K)
    [0] Sair 
    =>'''
    return int(input(dedent(conversor)))

def menu_final():
    print(f'\n{20*'='} CONVERSOR {20*'='}')
    conversor = f'''\
    {15*'='} TEMPERATURA FINAL {15*'='}
    [1] Celsius (C)
    [2] Fahreinheit (F)
    [3] Kelvin (K)
    [0] Sair
    =>'''
    return int(input(dedent(conversor)))

def celsius_fahrenheit():
    celsius = float(input('Temperatura Inicial: '))
    fahrenheit = 9/5 * celsius + 32
    print(f'\n{20*'='} CONVERSOR {20*'='}')
    print(f'Temperatura em Fahrenheit: {fahrenheit:.2f}°F')

def celsius_kelvin():
    celsius = float(input('Temperatura Inicial: '))
    kelvin = celsius + 273.15
    print(f'\n{20*'='} CONVERSOR {20*'='}')
    print(f'Temperatura em Kelvin: {kelvin:.2f}K')

def fahrenheit_celsius():
    fahrenheit = float(input('Temperatura Inicial: '))
    celsius = (fahrenheit - 32)*(5/9) 
    print(f'\n{20*'='} CONVERSOR {20*'='}')
    print(f'Temperatura em Celsius: {celsius:.2f}°C')

def fahrenheit_kelvin():
    fahrenheit = float(input('Temperatura Inicial: '))
    kelvin = (fahrenheit - 32)*(5/9) + 273.15
    print(f'\n{20*'='} CONVERSOR {20*'='}')
    print(f'Temperatura em Kelvin: {kelvin:.2f}°K')

def kelvin_celsius():
    kelvin = float(input('Temperatura Inicial: '))
    celsius = kelvin - 273.15
    print(f'\n{20*'='} CONVERSOR {20*'='}')
    print(f'Temperatura em Celsius: {celsius:.2f}°C')

def kelvin_fahrenheit():
    kelvin = float(input('Temperatura Inicial: '))
    fahrenheit = (kelvin - 273.15)*(9/5) + 32
    print(f'\n{20*'='} CONVERSOR {20*'='}')
    print(f'Temperatura em Fahrenheit: {fahrenheit:.2f}°F')

while True:
    opções_validas = set([0,1,2,3])
    opção_inicial = menu_inicial()
    
    if opção_inicial in opções_validas:
        if opção_inicial == 0:
            print('Saindo do conversor ...')
            exit()
        else:
            while True:
                opção_final = menu_final()
            
                if opção_inicial == opção_final:
                    print('====== Selecione temperaturas diferentes! ======')
                
                elif opção_final == 0:
                    print('Saindo do conversor ...')
                    exit()
                
                elif opção_inicial == 1 and opção_final == 2:
                    celsius_fahrenheit()
                    break
            
                elif opção_inicial == 1 and opção_final == 3:
                    celsius_kelvin()
                    break
            
                elif opção_inicial == 2 and opção_final == 1:
                    fahrenheit_celsius()
                    break
            
                elif opção_inicial == 2 and opção_final == 3:
                    fahrenheit_kelvin()
                    break
            
                elif opção_inicial == 3 and opção_final == 1:
                    kelvin_celsius()
                    break
            
                elif opção_inicial == 3 and opção_final == 2:
                    kelvin_fahrenheit()
                    break
                
                else:
                    print('\n====== Opção inválida ======')
    else:
        print('\n====== Opção Inválida! ======')

