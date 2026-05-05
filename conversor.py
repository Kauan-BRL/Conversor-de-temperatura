from textwrap import dedent
from sys import exit

def c_f(n):  print(f'\nTemperatura em Fahrenheit: {9/5 * n + 32:.2f}°F')
def c_k(n):  print(f'\nTemperatura em Kelvin: {n + 273.15:.2f}K')
def f_c(n):  print(f'\nTemperatura em Celsius: {(n - 32)*(5/9) :.2f}°C')
def f_k(n):  print(f'\nTemperatura em Kelvin: {(n - 32)*(5/9) + 273.15:.2f}°K')
def k_c(n):  print(f'\nTemperatura em Celsius: {n - 273.15:.2f}°C')
def k_f(n):  print(f'\nTemperatura em Fahrenheit: {(n - 273.15)*(9/5) + 32:.2f}°F')

CONVERSOES = {
    (1,2):c_f, (1,3):c_k,
    (2,1):f_c, (2,3):f_k,
    (3,1):k_c, (3,2):k_f
}

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

while True:
    try:
        opções_validas = {0,1,2,3}
        opção_inicial = menu_inicial()
        
        if opção_inicial == 0:
                print('Saindo do conversor ...')
                exit()
        
        if opção_inicial in opções_validas:
            while True:
                opção_final = menu_final()
                
                if opção_final == 0:
                    print('Saindo do conversor ...')
                    exit()

                if opção_inicial == opção_final:
                    print('====== Selecione escalas diferentes! ======')
                
                if opção_final in opções_validas:
                    if (opção_inicial, opção_final) in CONVERSOES:
                        temp_ini = float(input('Temperatura Inicial: '))
                        função = CONVERSOES[(opção_inicial, opção_final)]
                        temp_fin = função(temp_ini)
                        break
                else:
                    print('\n====== Digite somente números disponíveis! ======')
        else:
            print('\n====== Digite somente números disponíveis! ======')
    except ValueError:
        print('\n====== Digite somente números! ======')




