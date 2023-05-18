import textwrap

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

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def menu (saque, deposito):
    
    menu = """
====== menu ======
Digite:
1 - Deposito
2 - Saque
3 - Extrato
4 - criar usuário
5 - criar conta
6 - listar contas
0 - Sair
==================
"""

    extrato ="====== extrato ======\n"

    escolha = int(input(menu))
    operações_por_dia = 0
    saldo = 1000
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        
        if escolha == 1:
            extrato, saldo = deposito(saldo, operações_por_dia, extrato)
            operações_por_dia += 1
        
        elif escolha == 2:
            extrato, saldo = saque(saldo, operações_por_dia, extrato)
            operações_por_dia += 1

        elif escolha == 3:
            print(extrato + f'Total:    R$:{saldo}\n' + '=====================')

        elif escolha == 4:
             criar_usuario(usuarios)

        elif escolha == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif escolha == 6:
            listar_contas(contas)
        
        elif escolha == 0:
            break

        else:
            print("comando inválido")

        escolha = int(input(menu))

menu(saque, deposito)
