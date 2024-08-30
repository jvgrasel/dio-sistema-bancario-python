import textwrap

def menu():
    menu = """.\

[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNovo usuário
[5]\tNova conta
[6]\tLista usuários
[0]\tSair
=> """
    return input(textwrap.dedent(menu))

def criar_usuario(usuarios):
    while True:
        cpf = input("Informe o CPF (somente números): ").strip()
        
        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido! O CPF deve conter 11 dígitos numéricos.")
            continue

        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            print("\nO CPF informado já foi cadastrado!")
            return

        nome = input("Informe o nome completo: ").strip()
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade-sigla estado): ").strip()

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("Usuário criado com sucesso!")
        return

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_usuarios(agencia, usuarios, contas):
    for usuario in usuarios:
        cpf = usuario['cpf']
        contas_do_usuario = [
            f"Conta: {conta['numero_conta']} (Agência: {agencia})"
            for conta in contas
            if conta['cpf'] == cpf
        ]
        contas_str = ", ".join(contas_do_usuario) if contas_do_usuario else "Nenhuma conta"
        print(f"CPF: {cpf}, Nome: {usuario['nome']}, Contas: {contas_str}")

def criar_conta(agencia, usuarios, contas):
    cpf = input("Informe o CPF do usuário para criar a conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nUsuário não encontrado!\nFavor cadastrar o usuário na opção 4")
        return

    numero_conta = len(contas) + 1  
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "cpf": cpf})

    print(f"=== Conta criada com sucesso! Número da conta: {numero_conta} ===")
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            criar_usuario(usuarios)
        elif opcao == "5":
            criar_conta(AGENCIA, usuarios, contas)
        elif opcao == "6":
            listar_usuarios(AGENCIA, usuarios, contas)
        elif opcao == "0":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
