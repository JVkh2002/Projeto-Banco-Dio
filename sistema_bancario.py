def saque(saldo, operações_por_dia, extrato):
    saque = int(input("Qual o valor do saque?: "))
    saldo = saldo
    extrato = extrato

    if saque < saldo:

        if operações_por_dia < 3:
            
            saldo -= saque
            print(f'Saque de R${saque} realizado.\n')
            extrato += f'Saque:    R$:{saque}\n'

        
        else:
            print("Número de operações por dia alcançado.")

        return extrato, saldo
            
    else:
        print("Saldo insuficiente.")

    return extrato, saldo

def deposito(saldo, operações_por_dia, extrato):
    deposito = int(input("Qual o valor do deposito?: "))
    saldo = saldo
    extrato = extrato
    
    if deposito > 0:
                
        if operações_por_dia < 3:

            if deposito <= 500:        
                saldo += deposito
                print(f'Deposito de R${deposito} realizado.\n')
                extrato += f'Deposito: R$:{deposito}\n'
                
            
            else:
                print("Depositos maiores que R$500 são inválidos.")

            return extrato, saldo
        
        else:
            print("Número de operações por dia alcançado.")

        return extrato, saldo

    else:
        print("número inválido")

    return extrato, saldo

def menu (saque, deposito):
    
    menu = """
====== menu ======
Digite:
1 - Deposito
2 - Saque
3 - Extrato
0 - Sair
==================
"""

    extrato ="====== extrato ======\n"

    escolha = int(input(menu))
    operações_por_dia = 0
    saldo = 1000

    while True:
        
        if escolha == 1:
            extrato, saldo = deposito(saldo, operações_por_dia, extrato)
            operações_por_dia += 1
        
        elif escolha == 2:
            extrato, saldo = saque(saldo, operações_por_dia, extrato)
            operações_por_dia += 1

        elif escolha == 3:
            print(extrato + f'Total:    R$:{saldo}\n' + '=====================')
        
        elif escolha == 0:
            break

        else:
            print("comando inválido")

        escolha = int(input(menu))

def novo_cliente(nome, endereco, cpf):
    nome = nome
    endereco = endereco
    cpf = cpf
    
    print(f'Novo cliente registrado:\nnome: {nome}\nendereço: {endereco}\ncpf: {cpf}')
    return nome, endereco, cpf

#novo_cliente("joão", "são paulo", 50020)

menu(saque, deposito)





