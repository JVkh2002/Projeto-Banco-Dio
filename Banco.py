saldo = 1000
operações_por_dia = 0
limite_deposito_dia = 0

menu = f"""
======== Menu ========
Digite:
1 - depositar
2 - sacar
3 - extrato
0 - sair
======================
"""

extrato = f"""
======== extrato ========
"""

opção = int(input(menu))
print()

while opção != 0:

    if opção > 0 and opção < 4:
 

        if opção == 1:
            valor = int(input("Qual o valor do deposito?: "))
            
            if valor > 0:
                    
                if operações_por_dia < 3:   

                    if limite_deposito_dia <= 1500:
                            
                        if valor <= 500:
                            saldo += valor
                            limite_deposito_dia += valor
                            deposito = f"Deposito: +R${valor}\n"
                            extrato += f'{deposito}'
                            print(f'{extrato}\nTotal:     R${saldo}')
                            operações_por_dia += 1
                                        
                        else:
                            print('Depositos maiores que R$500 não são permitidos.')

                    else:
                        print("limite diário de R$1500 para deposito alcançado.")

                else:
                    print('Número de operações diárias permitidas alcançado.')

            else:
                print('valor invalido')
            
        elif opção == 2:
            valor = int(input("Qual o valor do saque?: "))

            if valor > 0:

                if operações_por_dia < 3:
                    
                    if valor <= saldo:
                        saldo -= valor
                        saque = f"Saque:    -R${valor}\n"
                        extrato += f'{saque}'
                        print(f'{extrato}\nTotal:     R${saldo}')
                        operações_por_dia += 1
                    
                    else:
                        print('saldo insuficiente')
                
                else:
                    print('Número de operações diárias permitidas alcançado.')
                
            else:
                print('valor invalido')

        if opção == 3:
            print(f'{extrato}\nTotal:     R${saldo}')

    else:
        print("opção invalida")

    opção = int(input(menu))



    