menu = '''
     ### ESCOLHA A OPERAÇÃO DESEJADA ###

     [1] Saque Conta-Corrente
     [2] Deposito
     [3] Extrato
     [0] Sair
'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao =="1":
        if numero_saques < LIMITE_SAQUES:
            valor_saque=float(input("Digite o valor que deseja sacar: "))       
            if (valor_saque >0 and valor_saque <=500):
                 if saldo >= valor_saque:
                       saldo-=valor_saque
                       print(f"Saque no valor de R$ {valor_saque:.2f}. \nFoi realizado com sucesso! \n",)
                       numero_saques +=1
                       extrato += f"Saque de R$ {valor_saque:.2f} realizado.\n"                  
                 else: print("SALDO INSUFICIENTE!\n")
            else: print(f"Valor incorreto! O limite de saque é R$ {limite}")               
        else: print("LIMITE DE SAQUE ATINGIDO!") 
    elif opcao == "2":
        valor_deposito=float(input("Digite o valor do deposito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Deposito no valor de R$ {valor_deposito:.2f}.\nRealizado com sucesso!")
            extrato += f"Deposito de R$ {valor_deposito:.2f} realizado.\n"
        else:
            print("Valor invalido! Tente novamente.") 
    elif opcao == "3":
        print("### EXTRADO DA CONTA ###\n")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == "0":
        print("Obrigado por utilizar nosso serviços.")
        break 
    else :
        print("Opção invalida! Tente novamente.")

