
clientes = []

def validar_login(login, senha):
    if login == 'admin' and senha == 'admin':
        return True
    else:
        return False


#função para exibir o menu
def exibir_menu():
    print('1 - Cadastrar cliente')
    print('2 - Listar clientes')
    print('3 - Sair')
    print('Digite a opção desejada: ')

def cadastrar_cliente():
    print('Cadastro de cliente')
    nome = input('Nome: ')
    login = input('login: ')
    endereco = input('Endereço completo(Rua, número, complemento, bairro, cidade, cep e ponto de referencia) ').split(',')
    telefone = input('Telefone: ')
    data = input('data de nascimento: ')
    cliente = {'nome': nome, 'login': login, 'endereco': endereco, 'telefone': telefone, 'data': data}
    print('Cliente cadastrado com sucesso !')
    return cliente

def mostrar_dados_cliente(nome):
    print('Dados do cliente')
    for cliente in clientes:
        if cliente['nome'] == nome:
            print(cliente)

    print('1 - Voltar ao menu')
    print('Digite a opção desejada: ')
    opcao = int(input())
    if opcao == 1:
        exibir_menu()


def listar_clientes():
    print('Lista de clientes')
    for cliente in clientes:
        print(cliente['nome'])
    
    print('1 - Mostrar dados de um cliente')
    print('2 - Voltar ao menu')
    print('Digite a opção desejada: ')
    opcao = int(input())
    if opcao == 1:
        print('Digite o Nome do cliente: ')
        nome = input()
        mostrar_dados_cliente(nome)
    elif opcao == 2:
        exibir_menu()



def main():
    while True:
        exibir_menu()
        opcao = int(input())
        if opcao == 1:
            clientes.append(cadastrar_cliente())
        elif opcao == 2:
            listar_clientes()
        elif opcao == 3:
            break
        else:
            print('Opção inválida')


if __name__ == '__main__':
    main()