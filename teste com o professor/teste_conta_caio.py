def cria_conta(nome, conta_numero, saldo, limite):
    conta = {'nome': nome, 'conta_corrente': conta_numero, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor
    print(f"Depósito de R$ {valor} realizado com sucesso! E saldo atual é R$ {conta['saldo']}")
    return conta

def saca(conta, valor):
    conta['saldo'] -= valor
    print(f"Saque de R$ {valor} realizado com sucesso! E saldo atual é R$ {conta['saldo']}")
    return conta

def extrato(conta):
    print(f"Saldo atual: R${conta["saldo"]}")
    return conta

nome = input("Digite seu nome: ")
conta_numero = input("Digite o número da conta: ")
saldo = float(input("Digite o saldo inicial: "))
limite = 10000

conta = cria_conta(nome, conta_numero, saldo, limite)

opcao = input("\nEscolha uma operação: \n1) Depositar \n2) Sacar \n3) Extrato \n: ")

if opcao == "1":
    valor = float(input("Digite o valor a depositar:"))
    conta = deposita(conta, valor)
elif opcao == "2":
    valor = float(input("Digite o valor a sacar: "))
    conta = saca(conta, valor)
elif opcao == "3":
    conta = extrato(conta)
else:
    print("Opção inválida.")