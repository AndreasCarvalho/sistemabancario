def exibir_menu():
    menu = """\n
[D] depositar
[S] Sacar
[E] Extrato
[NC] Nova conta
[LC]listar contas
[NU] Novos Usuarios
[Q] Sair
==>"""
    return input(menu).upper()

def depositar(saldo, valor , extrato, /):
    if valor >0:
        saldo += valor
        extrato += f"deposito R${valor:.2f}\n"
        print(f"\n === Deposito realizado com sucesso ! ===")
    else:
        print("operação falho ! formato invalido")

    return saldo, extrato

def sacar(*, saldo , valor  , extrato , limite , numero_saque , limite_saque):
    excedeu_saldo = valor >saldo
    execedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque

    if excedeu_saldo:
        print("voce nao tem saldo sufucinte")
    elif execedeu_limite:
        print("o valor do saque excedeu o limite diario")
    elif excedeu_saque:
        print("numero de saque maximo execedido")
    elif valor > 0 :
        saldo -= valor
        extrato+= f"saque: R${valor:.2f}\n"
        numero_saque+=1
        print("saque realizado com  sucesso")

    return saldo , extrato

def exibir_extrato(saldo, / , *, extrato):
    print(f"\n=============EXTRATO============")
    print(f"Nao foram realizadas movimentações "if not extrato else extrato)
    print(f"\nSaldo R${saldo:.2f}")
    print("=====================================")

def criar_usuario(usuarios):
    cpf = input("informe o cpf (somente numeros) :")
    usuario = filtar_usuario(cpf , usuario)

    if usuario:
        print("\n ja existe usuario com este CPF !!!")
        return

    nome = input("informe o nome completo :")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa) :")
    endereço = input("informe o endereço (logradouro , num , bairro , cidade , estado ) :")

    usuarios.append({"nome": nome , "data_nascimento": data_nascimento , "cpf": cpf, "endereço" : endereço })
    print("usuario cadastrado com sucesso!!")


def filtar_usuario(cpf , usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia , numero_conta , usuarios):
    cpf = input("informe o CPF do usuario :")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("\n ===Conta criada com sucesso ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("usuario nao encontrado !")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
                    Agencia : \t{conta['agencia']}
                    C/C:\t\t{conta['numero_conta']}
                    Titular :\t{conta['usuario']['nome']}"""

        print("="*100)
        print(linha)

def main():
    limite_saque = 3
    agencia = "0001"
    saldo = 0
    limite =500
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "D":
            valor = float(input("informe o valor do deposito :"))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("informe o valor do saque :"))
            saldo , extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=limite_saque,
            )

        elif opcao=="E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao =="NU":
            criar_usuario(usuarios)

        elif opcao == "NC":
            numero_conta = len(contas)+1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao=="LC":
            listar_contas(contas)

        elif opcao=="Q":
            break

        else:
            print("operação invalida")

main()
