menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! Excedeu o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("Não foram realidas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f} e seu limite é de R$ {limite:.2f}")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")